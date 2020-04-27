from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from recommender_engine import do_recommendation
from dialogflow_client import do_dialogflow_analysis
from fulfillment import do_fulfillment
from django.shortcuts import render
from .models import Student, University_Course

from .serializers import StudentSerializer, University_CourseSerializer, CountrySerializer
from google.protobuf.json_format import MessageToJson
import json
import time
from django.db.models import Q


@csrf_exempt
def index(request):
    return render(request, 'index.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def load_regions(request):
    region_list = University_Course.objects.values('region').distinct()
    return render(request, 'recommendation.html', {'region_list': region_list})

@csrf_exempt
def load_countrys(request):
    region = request.POST['region']
    country_list = University_Course.objects.filter(region=region).values('country').distinct()
    serializer = CountrySerializer(country_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def result(request):
    region = request.POST['region']
    country = request.POST['country']
    ielts = request.POST['ielts']
    toefl = request.POST['toefl']
    work_study = request.POST['work_study']
    min_tution_fee = request.POST['min_tution_fee']
    max_tution_fee = request.POST['max_tution_fee']

    print("===>" + json.dumps(request.POST))

    result_list = University_Course.objects.filter(region=region).all()
    if ielts:
        result_list = result_list.filter(min_IELTS__lte=ielts)
    if toefl:
        result_list = result_list.filter(
            Q(min_TOEFL__isnull=True) | Q(min_TOEFL__lte=toefl))
    if min_tution_fee:
        result_list = result_list.filter(
            Q(average_tuition_fee__isnull=True) |
            Q(average_tuition_fee__gte=min_tution_fee)
        )
    if max_tution_fee:
        result_list = result_list.filter(
            Q(average_tuition_fee__isnull=True) |
            Q(average_tuition_fee__lte=max_tution_fee)
        )

    return render(request, 'result.html', {'result_list': result_list})

@csrf_exempt
def university_list(request):
    if request.method == 'GET':
        universities = University_Course.objects.all()
        serializer = University_CourseSerializer(universities, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status = 404)

@csrf_exempt
def recommendation(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        uni_course_list = University_Course.objects.values()

        # get recommended list from the knowledge engine
        recommended_list = do_recommendation(uni_course_list, request_data)
        serializer = University_CourseSerializer(recommended_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status = 404)

@csrf_exempt
def chat(request):
    if request.method =='POST':
        enquiry_text =''
        try:
            #request_data = JSONParser().parse(request) # for api calls from jmeter and postman
            request_data = json.loads(request.body.decode('utf-8'))
            enquiry_text = request_data['enquiry']
        except:
            enquiry_text = request.POST['enquiry']
        
        if enquiry_text == '':
            raise Exception('Cannot detect enquiry')

        # get intent and slot detection from dialogflow client
        response = do_dialogflow_analysis(enquiry_text)

        jsonObj = MessageToJson(response.query_result)  # type is google.cloud.dialogflow_v2.types.QueryResult
        response_json = json.loads(jsonObj)
        parameters = response_json['parameters']
        # parameter['UniversityName'], parameters['CourseType']
        intent = response_json['intent']['displayName']
        print("intent is {0}".format(intent))
        print("parameters is {0}".format(parameters))

        # implement fulfillment
        output = do_fulfillment(intent, parameters)
        return HttpResponse(output)

        

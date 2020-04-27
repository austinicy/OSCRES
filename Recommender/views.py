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
        request_data['ielts'] = float(request_data['ielts'] or -1.0)
        request_data['toefl'] = float(request_data['toefl'] or -1.0)
        request_data['min_tution_fee'] = float(request_data['min_tution_fee'] or -1.0)
        request_data['max_tution_fee'] = float(request_data['max_tution_fee'] or -1.0)
        request_data['math'] = float(request_data['math'] or -1.0)
        request_data['chinese'] = float(request_data['chinese'] or -1.0)
        request_data['english'] = float(request_data['english'] or -1.0)
        request_data['physics'] = float(request_data['physics'] or -1.0)
        request_data['chemistry'] = float(request_data['chemistry'] or -1.0)
        request_data['biology'] = float(request_data['biology'] or -1.0)
        request_data['history'] = float(request_data['history'] or -1.0)
        request_data['geogrophy'] = float(request_data['geogrophy'] or -1.0)
        request_data['politics'] = float(request_data['politics'] or -1.0)
        request_data['art'] = float(request_data['art'] or -1.0)

        uni_course_list = University_Course.objects.values()
        for dicts in uni_course_list: 
            if int(dicts['academic_reputation_rank'] or 0) < 100:
                dicts['academic_reputation_rank'] = 'high'
            elif int(dicts['academic_reputation_rank'] or 0) > 300:
                dicts['academic_reputation_rank'] = 'low'
            elif int(dicts['academic_reputation_rank'] or 0) == 0:
                dicts['academic_reputation_rank'] = ''
            else:
                dicts['academic_reputation_rank'] = 'medium'

            if int(dicts['employer_reputation_rank'] or 0) < 100:
                dicts['employer_reputation_rank'] = 'high'
            elif int(dicts['employer_reputation_rank'] or 0) > 300:
                dicts['employer_reputation_rank'] = 'low'
            elif int(dicts['employer_reputation_rank'] or 0) == 0:
                dicts['employer_reputation_rank'] = ''
            else:
                dicts['employer_reputation_rank'] = 'medium'
                
            if int(dicts['faculty_student_rank'] or 0) < 100:
                dicts['faculty_student_rank'] = 'high'
            elif int(dicts['faculty_student_rank'] or 0) > 300:
                dicts['faculty_student_rank'] = 'low'
            elif int(dicts['faculty_student_rank'] or 0) == 0:
                dicts['faculty_student_rank'] = ''
            else:
                dicts['faculty_student_rank'] = 'medium'
                
            if int(dicts['citation_rank'] or 0) < 100:
                dicts['citation_rank'] = 'high'
            elif int(dicts['citation_rank'] or 0) > 300:
                dicts['citation_rank'] = 'low'
            elif int(dicts['citation_rank'] or 0) == 0:
                dicts['citation_rank'] = ''
            else:
                dicts['citation_rank'] = 'medium'
                
            if int(dicts['international_faculty_rank'] or 0) < 100:
                dicts['international_faculty_rank'] = 'high'
            elif int(dicts['international_faculty_rank'] or 0) > 300:
                dicts['international_faculty_rank'] = 'low'
            elif int(dicts['international_faculty_rank'] or 0) == 0:
                dicts['international_faculty_rank'] = ''
            else:
                dicts['international_faculty_rank'] = 'medium'
                
            if int(dicts['international_student_rank'] or 0) < 100:
                dicts['international_student_rank'] = 'high'
            elif int(dicts['international_student_rank'] or 0) > 300:
                dicts['international_student_rank'] = 'low'
            elif int(dicts['international_student_rank'] or 0) == 0:
                dicts['international_student_rank'] = ''
            else:
                dicts['international_student_rank'] = 'medium'

            if float(dicts['cost_of_living_index'] or 0) <= 75:
                dicts['cost_of_living_index'] = 'low'
            elif float(dicts['cost_of_living_index'] or 0) > 100:
                dicts['cost_of_living_index'] = 'high'
            elif int(dicts['cost_of_living_index'] or 0) == 0:
                dicts['cost_of_living_index'] = ''
            else:
                dicts['cost_of_living_index'] = 'medium'

            if float(dicts['international_student_percentage'] or 0) <= 0.15:
                dicts['international_student_percentage'] = 'low'
            elif float(dicts['international_student_percentage'] or 0) > 0.31:
                dicts['international_student_percentage'] = 'high'
            elif int(dicts['international_student_percentage'] or 0) == 0:
                dicts['international_student_percentage'] = ''
            else:
                dicts['international_student_percentage'] = 'medium'

            if dicts['offer_work_study_program'] == 1:
                dicts['offer_work_study_program'] = 'yes'
            else:
                dicts['offer_work_study_program'] = 'no'

            dicts['min_IELTS'] = float(dicts['min_IELTS'] or 999.0)
            dicts['min_TOEFL'] = float(dicts['min_TOEFL'] or 999.0)
            dicts['average_tuition_fee'] = float(dicts['average_tuition_fee'] or -1.0)
            dicts['acceptance_rate'] = float(dicts['acceptance_rate'] or -1.0)

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
            request_data = JSONParser().parse(request) # for api calls from jmeter and postman
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

        

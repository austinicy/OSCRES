from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from recommender_engine import do_recommendation
from dialogflow_client import do_dialogflow_analysis
from fulfillment import do_fulfillment
from django.shortcuts import render
from .models import Student, University_Course
from .serializers import StudentSerializer, University_CourseSerializer
from google.protobuf.json_format import MessageToJson
import json


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
        request_data = JSONParser().parse(request)
        enquiry_text = request_data['enquiry']

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

        

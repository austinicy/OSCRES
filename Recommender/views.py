from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from recommender_engine import do_recommendation
from django.shortcuts import render
from .models import Student, University_Course
from .serializers import StudentSerializer, University_CourseSerializer


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
        # get recommended list
        recommended_list = do_recommendation(uni_course_list, request_data)
        serializer = University_CourseSerializer(recommended_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status = 404)


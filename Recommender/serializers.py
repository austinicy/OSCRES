from rest_framework import serializers
from .models import Student
from .models import University_Course
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'preferred_country', 'ielts_score']

class University_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['id', 'name','country', 'city', 'min_IELTS', 'min_TOEFL', 'status', 'field_of_study']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['country']
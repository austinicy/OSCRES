from rest_framework import serializers
from .models import Student
from .models import University_Course

# Not needed for now
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'preferred_country', 'ielts_score']

class University_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['id','name','country','population_size','age','status','academic_reputation_score','academic_reputation_rank','employer_reputation_score','employer_reputation_rank','faculty_student_score','faculty_student_rank','citation_score','citation_rank','international_faculty_score','international_faculty_rank','international_student_score','international_student_rank','overall_score','city','region','cost_of_living_index','international_student_percentage','field_of_study','subject','program_name','min_IELTS','min_TOEFL','min_GPA','campus_setting','offer_work_study_program','average_tuition_fee','offer_airport_pickup','acceptance_rate']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['country']

def StudentDeSerializer(data):
    return Student(
        region = data['region'] if 'region' in data else '',
        country = data['country'] if 'country' in data else '',
        academic_reputation_rank  = data['academic_reputation_rank'],
        employer_reputation_rank  = data['employer_reputation_rank'],
        faculty_student_rank  = data['faculty_student_rank'],
        international_faculty_rank  = data['international_faculty_rank'],
        international_student_rank  = data['international_student_rank'],
        citation_rank  = data['citation_rank'],
        ielts  = data['ielts'],
        toefl  = data['toefl'],
        work_study  = data['work_study'],
        min_tution_fee  = data['min_tution_fee'],
        max_tution_fee  = data['max_tution_fee'],
        international_student_percentage  = data['international_student_percentage'],
        cost_index  = data['cost_index'],
        math  = data['math'],
        chinese  = data['chinese'],
        english  = data['english'],
        physics  = data['physics'],
        chemistry  = data['chemistry'],
        biology  = data['biology'],
        history  = data['history'],
        geogrophy  = data['geogrophy'],
        politics  = data['politics'],
        art  = data['art']
        )
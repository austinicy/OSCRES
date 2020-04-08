from django.http import HttpResponse

from recommender import do_recommendation

def hello(request):
    from University_Course.models import University_Course
    from Student.models import Student
    uni_course_list = University_Course.objects.values()
    print(uni_course_list)

    student = Student(1, "Norman", "UK", 3.8)

    recommended_list = do_recommendation(uni_course_list, student)
    print(recommended_list)
    return HttpResponse("your recommended shcools are: " + " ".join(recommended_list))
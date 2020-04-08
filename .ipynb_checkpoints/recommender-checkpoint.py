from pyknow import *

class University_Course_F(Fact):
    name = Field(str)
    country = Field(str)
    city = Field(str)
    region = Field(str)
    academic_reputatin_socre = Field(float)
    academic_reputatin_rank = Field(int)
    overall_score = Field(float)
    field_of_study = Field(str)
    subject = Field(str)
    min_IETLTS = Field(float)
    accomodation = Field(bool)

class Student_F(Fact):
    name = Field(str)
    preferred_country = Field(str)
    preferred_shool = Field(str)
    IELTS_score = Field(float)
    need_accommodation = Field(bool)

class Recommendation(KnowledgeEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recommended = False

    @Rule(AS.s << Student_F(IELTS_score = MATCH.IELTS_score), TEST(lambda IELTS_score: IELTS_score >= min_IELTS), salience =1)
    def testRule1(self):
        print("you rock")
        self.recommended = True

def do_recommendation(uni_list, student):
    recommendation_list = []
    for record in uni_list:
        uni_name = record["name"][0]
        min_IELTS = record["min_ielts"][0]
        recommender = Recommendation()
        recommender.reset()
        recommender.run()
        recommender.facts
        if (recommender.recommended):
            recommendation_list.append(uni_name)


# driver program
from University_Course.models import University_Course
from Student/models import Student
uni_course_list = University_Course.objects.values()
print(uni_course_list)

student = Student("Norman", "UK", 5.0)

recommended_list = do_recommendation(uni_course_list, student)
print(recommended_list)

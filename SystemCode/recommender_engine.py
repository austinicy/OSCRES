from pyknow import *

class UniversityCourse_F(Fact):
    name = Field(str)
    country = Field(str)
    city = Field(str)
    region = Field(str)
    academic_reputatin_socre = Field(float)
    academic_reputatin_rank = Field(int)
    overall_score = Field(float)
    field_of_study = Field(str)
    subject = Field(str)
    min_IELTS = Field(float)
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

    @Rule(AS.s << Student_F(IELTS_score = MATCH.IELTS_score), 
        AS.u << UniversityCourse_F(min_IELTS = MATCH.min_IELTS), 
        TEST(lambda IELTS_score, min_IELTS: IELTS_score >= min_IELTS), salience =1)
    def testRule1(self):
        print("you rock")
        self.recommended = True


def do_recommendation(uni_list, student):
    recommendation_list = []
    for uni in uni_list:
        recommender_engine = Recommendation()
        recommender_engine.reset()
        recommender_engine.declare(mapStudentFact(student))
        recommender_engine.declare(mapUniversityCourseFact(uni))
        recommender_engine.run()
        recommender_engine.facts
        if (recommender_engine.recommended):
            recommendation_list.append(uni)
    return recommendation_list


def mapStudentFact(student):
    return Student_F(
        IELTS_score = student["ielts_score"],
        preferred_country = student["preferred_country"]
        )

def mapUniversityCourseFact(uni):
    return UniversityCourse_F(
        min_IELTS = uni["min_ielts"],
        country = uni["country"]
        )
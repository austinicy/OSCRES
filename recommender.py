from pyknow import *

class University(Fact):
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

class Student(Fact):
    name = Field(str)
    prefered_country = Field(str)
    preferred_shool = Field(str)
    IETLS_score = Field(float)
    need_accommodation = Field(bool)

class Recommendation(KnowledgeEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @Rule(AS.s << Student(IETLS_score = MATCH.IETLS_score), TEST(lamda IETLS_score: IETLS_score < min_IETLTS)):
    def not_enough_IETLTS(self):
        print("you suck")


# driver program
import pandas as pd
uni_list = pd.read_csv("shools.csv")
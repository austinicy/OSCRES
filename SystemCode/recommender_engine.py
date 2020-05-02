from pyknow import *
from fuzzy_values import *
import operator

class Match_F(Fact):
    pass

class UniversityCourse_F(Fact):
    pass

class Student_F(Fact):
    pass

class Recommendation(KnowledgeEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefered = False
        self.recommendedbyAcademic = False
        self.recommendedbyFinancial = False
        self.matchBasic = False
        self.matchingCount = 0

 

    @Rule(AS.s << Student_F(prefered_region = MATCH.prefered_region), 
        TEST(lambda prefered_region:prefered_region  == ''),
        salience =5)
    def regionRule2(self):
        print('    : regionRule2')
        self.declare(Match_F(is_prefered_region = True))

    @Rule(AS.s << Student_F(prefered_country = MATCH.prefered_country), 
        TEST(lambda prefered_country:prefered_country  == ''),
        salience =5)
    def countryRule2(self):
        print('    : countryRule2')
        self.declare(Match_F(is_prefered_country = True))

    @Rule(AS.s << Student_F(ielts = MATCH.ielts), 
        TEST(lambda ielts:ielts <0),
        AS.s << Student_F(toefl = MATCH.toefl), 
        TEST(lambda toefl:toefl <0),
        salience =5)
    def englishRule2(self):
        print('    : englishRule2')
        self.declare(Match_F(satisfy_english = True))

    @Rule(AS.s << Student_F(prefered_academic_reputation_rank = MATCH.prefered_academic_reputation_rank), 
        TEST(lambda prefered_academic_reputation_rank: 
            prefered_academic_reputation_rank == 'none'),
        salience =5)
    def academicreputationrankRule2(self):
        print('    : academicreputationrankRule2')
        self.declare(Match_F(is_prefered_academic_reputation_rank = True))

    @Rule(AS.s << Student_F(prefered_employer_reputation_rank = MATCH.prefered_employer_reputation_rank), 
        TEST(lambda prefered_employer_reputation_rank:
            prefered_employer_reputation_rank == 'none'),
        salience =5)
    def employerreputationrankRule2(self):
        print('    : employerreputationrankRule2')
        self.declare(Match_F(is_prefered_employer_reputation_rank = True))

    @Rule(AS.s << Student_F(prefered_faculty_student_rank = MATCH.prefered_faculty_student_rank), 
        TEST(lambda prefered_faculty_student_rank:
            prefered_faculty_student_rank == 'none'),
        salience =5)
    def facultystudentrankRule2(self):
        print('    : facultystudentrankRule2')
        self.declare(Match_F(is_prefered_faculty_student_rank = True))

    @Rule(AS.s << Student_F(prefered_international_faculty_rank = MATCH.prefered_international_faculty_rank), 
        TEST(lambda prefered_international_faculty_rank:
            prefered_international_faculty_rank == 'none'),
        salience =5)
    def internationalfacultyrankRule2(self):
        print('    : internationalfacultyrankRule2')
        self.declare(Match_F(is_prefered_international_faculty_rank = True))

    @Rule(AS.s << Student_F(prefered_international_student_rank = MATCH.prefered_international_student_rank), 
        TEST(lambda prefered_international_student_rank: 
            prefered_international_student_rank == 'none'),
        salience =5)
    def internationalstudentrankRule2(self):
        print('    : internationalstudentrankRule2')
        self.declare(Match_F(is_prefered_international_student_rank = True))

    @Rule(AS.s << Student_F(prefered_citation_rank = MATCH.prefered_citation_rank), 
        TEST(lambda prefered_citation_rank:
            prefered_citation_rank == 'none'),
        salience =5)
    def citationrankRule2(self):
        print('    : citationrankRule2')
        self.declare(Match_F(is_prefered_citation_rank = True))

    @Rule(AS.s << Student_F(prefered_min_tution_fee = MATCH.prefered_min_tution_fee), 
        TEST(lambda prefered_min_tution_fee:prefered_min_tution_fee <0), 
        AS.s << Student_F(prefered_max_tution_fee = MATCH.prefered_max_tution_fee), 
        TEST(lambda prefered_max_tution_fee:prefered_max_tution_fee <0), 
        salience =5)
    def tutionfeeRule2(self):
        print('    : tutionfeeRule2')
        self.declare(Match_F(is_prefered_tuition_fee = True))

    @Rule(AS.s << Student_F(prefered_international_student_percentage = MATCH.prefered_international_student_percentage), 
        TEST(lambda prefered_international_student_percentage: 
            prefered_international_student_percentage == 'none'), 
        salience =5)
    def internationalstudentpercentageRule2(self):
        print('    : internationalstudentpercentageRule2')
        self.declare(Match_F(is_prefered_international_student_percentage = True))

    @Rule(AS.s << Student_F(prefered_cost_index = MATCH.prefered_cost_index), 
        TEST(lambda prefered_cost_index,: 
            prefered_cost_index == 'none'), 
        salience =5)
    def costoflivingRule2(self):
        print('    : costoflivingRule2')
        self.declare(Match_F(is_prefered_cost_index = True))

    @Rule(AS.s << Student_F(prefered_work_study = MATCH.prefered_work_study), 
        TEST(lambda prefered_work_study: 
            prefered_work_study == 'none'),
        salience =5)
    def workstudyRule2(self):
        print('    : workstudyRule2')
        self.declare(Match_F(is_offering_work_study = True))


#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------


    @Rule(AS.s << Student_F(prefered_region = MATCH.prefered_region), 
        AS.u << UniversityCourse_F(region = MATCH.region), 
        TEST(lambda prefered_region, region: prefered_region == region),
        salience =5)
    def regionRule(self):
        print('    : regionRule')
        self.declare(Match_F(is_prefered_region = True))

    @Rule(AS.s << Student_F(prefered_country = MATCH.prefered_country), 
        AS.u << UniversityCourse_F(country = MATCH.country), 
        TEST(lambda prefered_country, country: prefered_country == country),
        salience =5)
    def countryRule(self):
        print('    : countryRule')
        self.declare(Match_F(is_prefered_country = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(ielts = MATCH.ielts), 
        AS.u << UniversityCourse_F(min_IELTS = MATCH.min_IELTS), 
        TEST(lambda ielts, min_IELTS: ielts >= min_IELTS),
        salience =5)
    def ieltsenglishRule(self):
        print('    : ielts_englishRule')
        self.declare(Match_F(satisfy_english = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(toefl = MATCH.toefl), 
        AS.u << UniversityCourse_F(min_TOEFL = MATCH.min_TOEFL), 
        TEST(lambda toefl, min_TOEFL: toefl >= min_TOEFL),
        salience =5)
    def toeflenglishRule(self):
        print('    : toefl_englishRule')
        self.declare(Match_F(satisfy_english = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_academic_reputation_rank = MATCH.prefered_academic_reputation_rank), 
        AS.u << UniversityCourse_F(academic_reputation_rank = MATCH.academic_reputation_rank), 
        TEST(lambda prefered_academic_reputation_rank, academic_reputation_rank: 
            (
                getAcademicRank(prefered_academic_reputation_rank)[0] <= academic_reputation_rank and 
                getAcademicRank(prefered_academic_reputation_rank)[1] >= academic_reputation_rank)
            ),
        salience =5)
    def academicreputationrankRule(self):
        print('    : academicreputationrankRule')
        self.declare(Match_F(is_prefered_academic_reputation_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_employer_reputation_rank = MATCH.prefered_employer_reputation_rank), 
        AS.u << UniversityCourse_F(employer_reputation_rank = MATCH.employer_reputation_rank),
        TEST(lambda prefered_employer_reputation_rank, employer_reputation_rank:
            (
                getEmployerRank(prefered_employer_reputation_rank)[0] <= employer_reputation_rank and 
                getEmployerRank(prefered_employer_reputation_rank)[1] >= employer_reputation_rank)
            ),
        salience =5)
    def employerreputationrankRule(self):
        print('    : employerreputationrankRule')
        self.declare(Match_F(is_prefered_employer_reputation_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_faculty_student_rank = MATCH.prefered_faculty_student_rank), 
        AS.u << UniversityCourse_F(faculty_student_rank = MATCH.faculty_student_rank),
        TEST(lambda prefered_faculty_student_rank, faculty_student_rank:
            (
                getFacultyStudentRank(prefered_faculty_student_rank)[0] <= faculty_student_rank and 
                getFacultyStudentRank(prefered_faculty_student_rank)[1] >= faculty_student_rank)
            ),
        salience =5)
    def facultystudentrankRule(self):
        print('    : facultystudentrankRule')
        self.declare(Match_F(is_prefered_faculty_student_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_international_faculty_rank = MATCH.prefered_international_faculty_rank), 
        AS.u << UniversityCourse_F(international_faculty_rank = MATCH.international_faculty_rank), 
        TEST(lambda prefered_international_faculty_rank, international_faculty_rank:
            (
                getInternationalFacultyRank(prefered_international_faculty_rank)[0] <= international_faculty_rank and 
                getInternationalFacultyRank(prefered_international_faculty_rank)[1] >= international_faculty_rank)
            ),
        salience =5)
    def internationalfacultyrankRule(self):
        print('    : internationalfacultyrankRule')
        self.declare(Match_F(is_prefered_international_faculty_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_international_student_rank = MATCH.prefered_international_student_rank), 
        AS.u << UniversityCourse_F(international_student_rank = MATCH.international_student_rank),
        TEST(lambda prefered_international_student_rank, international_student_rank: 
            (
                getInternationalStudentRank(prefered_international_student_rank)[0] <= international_student_rank and 
                getInternationalStudentRank(prefered_international_student_rank)[1] >= international_student_rank)
            ),
        salience =5)
    def internationalstudentrankRule(self):
        print('    : internationalstudentrankRule')
        self.declare(Match_F(is_prefered_international_student_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_citation_rank = MATCH.prefered_citation_rank), 
        AS.u << UniversityCourse_F(citation_rank = MATCH.citation_rank),
        TEST(lambda prefered_citation_rank, citation_rank:
            (
                getCitationRank(prefered_citation_rank)[0] <= citation_rank and 
                getCitationRank(prefered_citation_rank)[1] >= citation_rank)
            ),
        salience =5)
    def citationrankRule(self):
        print('    : citationrankRule')
        self.declare(Match_F(is_prefered_citation_rank = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_min_tution_fee = MATCH.prefered_min_tution_fee), 
        AS.u << UniversityCourse_F(average_tuition_fee = MATCH.average_tuition_fee), 
        TEST(lambda prefered_min_tution_fee, average_tuition_fee: prefered_min_tution_fee < average_tuition_fee), 
        AS.s << Student_F(prefered_max_tution_fee = MATCH.prefered_max_tution_fee), 
        TEST(lambda prefered_max_tution_fee, average_tuition_fee: prefered_max_tution_fee > average_tuition_fee), 
        salience =5)
    def tutionfeeRule(self):
        print('    : tutionfeeRule')
        self.declare(Match_F(is_prefered_tuition_fee = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_international_student_percentage = MATCH.prefered_international_student_percentage), 
        AS.u << UniversityCourse_F(international_student_percentage = MATCH.international_student_percentage), 
        TEST(lambda prefered_international_student_percentage, international_student_percentage: 
            (
                getInternationalStudentPercentage(prefered_international_student_percentage)[0] <= international_student_percentage and 
                getInternationalStudentPercentage(prefered_international_student_percentage)[1] >= international_student_percentage)
            ), 
        salience =5)
    def internationalstudentpercentageRule(self):
        print('    : internationalstudentpercentageRule')
        self.declare(Match_F(is_prefered_international_student_percentage = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_cost_index = MATCH.prefered_cost_index), 
        AS.u << UniversityCourse_F(cost_of_living_index = MATCH.cost_of_living_index), 
        TEST(lambda prefered_cost_index, cost_of_living_index: 
            (
                getCostOfLiving(prefered_cost_index)[0] <= cost_of_living_index and 
                getCostOfLiving(prefered_cost_index)[1] >= cost_of_living_index)
            ), 
        salience =5)
    def costoflivingRule(self):
        print('    : costoflivingRule')
        self.declare(Match_F(is_prefered_cost_index = True))
        self.matchingCount += 1

    @Rule(AS.s << Student_F(prefered_work_study = MATCH.prefered_work_study), 
        AS.u << UniversityCourse_F(offer_work_study_program = MATCH.offer_work_study_program), 
        TEST(lambda prefered_work_study, offer_work_study_program: 
            getWorkStudy(prefered_work_study) == offer_work_study_program),
        salience =5)
    def workstudyRule(self):
        print('    : workstudyRule')
        self.declare(Match_F(is_offering_work_study = True))
        self.matchingCount += 1

#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------


    @Rule(AND(
        Match_F(satisfy_english = True)
        ,Match_F(is_prefered_region = True)
        ,Match_F(is_prefered_country = True)
        ,Match_F(is_prefered_tuition_fee = True)
        ,Match_F(is_prefered_international_student_percentage = True)
        ,Match_F(is_prefered_cost_index = True)
        ,Match_F(is_prefered_academic_reputation_rank = True)
        ,Match_F(is_prefered_employer_reputation_rank = True)
        ,Match_F(is_prefered_faculty_student_rank = True)
        ,Match_F(is_prefered_international_faculty_rank = True)
        ,Match_F(is_prefered_international_student_rank = True)
        ,Match_F(is_prefered_citation_rank = True)
        ,Match_F(is_offering_work_study = True)
        ), salience =4)
    def PreferredRule(self):
        print("belong to [prefered]")
        self.prefered = True

    @Rule(AND(
        Match_F(satisfy_english = True)
        ,OR(Match_F(is_prefered_country = True),Match_F(is_prefered_region = True))
        ,Match_F(is_prefered_cost_index = True)
        ,Match_F(is_prefered_academic_reputation_rank = True)
        ,Match_F(is_prefered_employer_reputation_rank = True)
        ,Match_F(is_prefered_faculty_student_rank = True)
        ,Match_F(is_prefered_international_faculty_rank = True)
        ,Match_F(is_prefered_international_student_rank = True)
        ,Match_F(is_prefered_citation_rank = True)
        ), salience =4)
    def AcademicSuggestedRule(self):
        print("belong to [recommendedbyAcademic]")
        self.recommendedbyAcademic = True

    @Rule(AND(
        Match_F(satisfy_english = True)
        ,OR(Match_F(is_prefered_country = True),Match_F(is_prefered_region = True))
        ,Match_F(is_prefered_tuition_fee = True)
        ,Match_F(is_prefered_cost_index = True)
        ,Match_F(is_offering_work_study = True)
        ), salience =4)
    def FinancialSuggestedRule(self):
        print("belong to [recommendedbyFinancial]")
        self.recommendedbyFinancial = True

    @Rule(AND(
        Match_F(satisfy_english = True)
        ,Match_F(is_prefered_region = True)
        ), salience =4)
    def FinancialSuggestedRule(self):
        print("belong to [recommendedbyBasic]")
        self.matchBasic = True



def field_recommendation(student):
    field = 'Unable to recommend based on your given subject scorings'
    if student['math'] > 80:
        if student['english'] > 80:
            if student['politics'] > 70:
                field = 'Economics & Econometrics'
            elif student['politics'] >= 0:
                field = 'Accounting & Finance'
        elif student['english'] >= 0:
            if student['politics'] > 70:
                field = 'Engineering & Technology'
            elif student['politics'] > 0:
                field = 'Computer Science & Information Systems'
    elif student['math'] >= 0:
        if student['politics'] > 70:
            if student['chinese'] > 70:
                field = 'Business & Management Studies'
            elif student['chinese'] >= 0:
                field = 'Law'
        elif student['politics'] >= 0:
            if student['chinese'] > 60:
                field = 'Arts & Humanities'
            elif student['chinese'] >= 0:
                field = 'Medicine'
    return field

def do_recommendation(uni_list, student):
    recommendation_list = []
    sorted_list = []
    count = 0
    print('Start RuleEngine')
    uni_name  =''
    field = field_recommendation(student)
    for uni in uni_list:
        if uni['name'] == uni_name:
            continue
        uni_name = uni['name'] 
        print('matching for --> ', uni_name)
        recommender_engine = Recommendation()
        recommender_engine.reset()
        recommender_engine.declare(mapStudentFact(student))
        recommender_engine.declare(mapUniversityCourseFact(uni))
        recommender_engine.run()
        if (recommender_engine.prefered):
            uni['status'] = 'Matched All preference'
            uni['subject'] = field
            uni['id'] = recommender_engine.matchingCount
            recommendation_list.append(uni)
            count += 1
        elif (recommender_engine.recommendedbyAcademic):
            uni['status'] = 'Matched Acedemic Preference'
            uni['subject'] = field
            uni['id'] = recommender_engine.matchingCount
            recommendation_list.append(uni)
            count += 1
        elif (recommender_engine.recommendedbyFinancial):
            uni['status'] = 'Matched Financial Preference'
            uni['subject'] = field
            uni['id'] = recommender_engine.matchingCount
            recommendation_list.append(uni)
        elif(recommender_engine.matchBasic):
            uni['status'] = 'Matched Minimum TOEFL/IELTS Entry Requirement'
            uni['subject'] = field
            uni['id'] = recommender_engine.matchingCount
            recommendation_list.append(uni)
            count += 1
        # if count >= 3:
        #     break

    if recommendation_list:
        sorted_list = sorted(recommendation_list, key=operator.itemgetter('id'), reverse=True)

    return sorted_list[:3]


def mapStudentFact(student):
    return Student_F(
        prefered_region = student["region"],
        prefered_country = student["country"],
        prefered_academic_reputation_rank = student["academic_reputation_rank"],
        prefered_employer_reputation_rank = student["employer_reputation_rank"],
        prefered_faculty_student_rank = student["faculty_student_rank"],
        prefered_international_faculty_rank = student["international_faculty_rank"],
        prefered_international_student_rank = student["international_student_rank"],
        prefered_citation_rank = student["citation_rank"],
        ielts = student["ielts"],
        toefl = student["toefl"],
        prefered_work_study = student["work_study"],
        prefered_min_tution_fee = student["min_tution_fee"],
        prefered_max_tution_fee = student["max_tution_fee"],
        prefered_international_student_percentage = student["international_student_percentage"],
        prefered_cost_index = student["cost_index"],
        # math = student["math"],
        # chinese = student["chinese"],
        # english = student["english"],
        # physics = student["physics"],
        # chemistry = student["chemistry"],
        # biology = student["biology"],
        # history = student["history"],
        # geogrophy = student["geogrophy"],
        # politics = student["politics"],
        # art = student["art"],
        # satisfy_english = False,
        # is_prefered_region = False,
        # is_prefered_country = False,
        # is_prefered_tuition_fee = True,
        # is_prefered_international_student_percentage = False,
        # is_prefered_cost_index = False,
        # has_prefered_region = False,
        # has_prefered_country = False,
        # has_prefered_academic_reputation_rank = False,
        # has_prefered_employer_reputation_rank = False,
        # has_prefered_faculty_student_rank = False,
        # has_prefered_international_faculty_rank = False,
        # has_prefered_international_student_rank = False,
        # has_prefered_citation_rank = False,
        # has_ielts = False,
        # has_toefl = False,
        # has_prefered_work_study = False,
        # has_prefered_min_tution_fee = False,
        # has_prefered_max_tution_fee = False,
        # has_prefered_international_student_percentage = False,
        # has_prefered_cost_index = False
        )

def mapUniversityCourseFact(uni):
    return UniversityCourse_F(
        name =  uni["name"],
        country =  uni["country"],
        city = uni["city"],
        region = uni["region"],
        academic_reputation_rank = uni["academic_reputation_rank"],
        employer_reputation_rank = uni["employer_reputation_rank"],
        faculty_student_rank = uni["faculty_student_rank"],
        international_faculty_rank = uni["international_faculty_rank"],
        international_student_rank = uni["international_student_rank"],
        citation_rank = uni["citation_rank"],
        field_of_study = uni["field_of_study"],
        subject = uni["subject"],
        min_IELTS = uni["min_IELTS"],
        min_TOEFL = uni["min_TOEFL"],
        accomodation = True,
        cost_of_living_index =  uni["cost_of_living_index"],
        international_student_percentage =  uni["international_student_percentage"],
        offer_work_study_program =  uni["offer_work_study_program"],
        average_tuition_fee =  uni["average_tuition_fee"]
    )
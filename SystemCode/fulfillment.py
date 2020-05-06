
from Recommender.models import Student, University_Course
import fuzzy_values

def join(list, attribute):
    res =""
    i =0
    while (i<len(list)):
        if i==0:
           res = list[i][attribute]
        elif list[i][attribute] not in res:
            res = res + ", \n" + list[i][attribute]
        i = i +1
    return res

def do_fulfillment(intent, params):
    if intent == 'GreetingIntent':
        response = "You can ask me anything you want to know about the universities. To see a list of sample questions, click the 'Sample Questions' button, or type 'sample questions'."
        return response
    if intent == 'ByeIntent':
        response = 'Thanks for using the system, enjoy your study. Bye!'
        return response

    if intent == 'SampleQuestionIntent':
        content = ''
        file = open("Miscellaneous/Chatbot_questions.txt", "r")
        for line in file:
            content = content + '\n' + line
        file.close()
        return content



    if intent=='CityIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni: 
                    if uni['city']:
                        return "{0} is located in {1}".format(uni['name'], uni['city'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName']) 
        return default_response
    
    if intent=='AcademicReputationIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni: 
                    if uni['academic_reputation_score'] and uni['academic_reputation_rank']:
                        return "{0} has an academic reputation score of {1} and academic rank of {2}".format(uni['name'], uni['academic_reputation_score'], uni['academic_reputation_rank'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='EmployerReputationIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni: 
                    if uni['employer_reputation_score'] and uni['employer_reputation_rank']:
                        return "{0} has an employer reputation score of {1} and employer rank of {2}".format(uni['name'], uni['employer_reputation_score'], uni['employer_reputation_rank'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='CampusSettingIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['campus_setting']:
                        return "The campus of {0} is {1}".format(uni['name'], uni['campus_setting'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
                
        return default_response

    if intent=='CostOfLivingIntent':
        default_response = 'I am sorry, please specify a proper city'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['City']:
            unis = University_Course.objects.filter(city__icontains=params['City']).values()
            for uni in unis:
                if uni: 
                    if uni['cost_of_living_index']:
                        return "The cost of living index of {0} is {1}".format(params['City'], uni['cost_of_living_index'])
                    return missing_value_response + ' about {0}'.format(params['City'])
        return default_response

    if intent=='GPAIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['min_GPA']:
                        if uni['min_GPA'] == 'no minimum':
                            return "There is no minimum GPA requirement to enroll {0}".format(uni['name'])
                        return "The minimum GPA requirement to enroll {0} is {1}".format(uni['name'], uni['min_GPA'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='IELTSIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['min_IELTS']:
                        return "The minimum IELTS requirement to enroll {0} is {1}".format(uni['name'], uni['min_IELTS'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='TOEFLIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['min_TOEFL']:
                        return "The minimum TOEFL requirement to enroll {0} is {1}".format(uni['name'], uni['min_TOEFL'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='InternationalStudentRatioIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['international_student_percentage']:
                        return "In {0}, international student take about {1}%".format(uni['name'], 100*uni['international_student_percentage'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='TuitionFeeIntent':
        default_response = 'I am sorry, please specify a proper university'
        missing_value_response = 'I am sorry, I did not find {0}'.format(intent.replace('Intent', ''))
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['average_tuition_fee']:
                        return "The average tuition fee of {0} is {1} USD".format(uni['name'], uni['average_tuition_fee'])
                    return missing_value_response + ' about {0}'.format(params['UniversityName'])
        return default_response

    if intent=='WorkStudyIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            for uni in unis:
                if uni:
                    if uni['offer_work_study_program'] == 1:
                        return "{0} offers Work Study Program".format(uni['name'])
                    else:
                        return "{0} does not offer Work Study Program".format(uni['name'])                    
        return default_response

    if intent=='StudyFieldIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            fields = join(unis, "field_of_study")
            return "{0} offers below fields of study: \n{1}".format(params['UniversityName'], fields)
        return default_response

    if intent=='SubjectIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName']).values()
            subjects = join(unis, "subject")
            return "{0} offers below subjects: \n{1}".format(params['UniversityName'], subjects)
        return default_response

    if intent=='UniversityIntent':
        default_response = 'I am sorry, but I do not understand your question. Please try again'
        print(params)
        if params['Country']:
            unis = University_Course.objects.filter(country__icontains=params['Country']).values()
            uni_names = join(unis, "name")
            return "In {0}, we are cooperating with below universities: \n{1}".format(params['Country'], uni_names)
        if params['Subject']:
            unis = University_Course.objects.filter(subject__icontains=params['Subject']).values()
            uni_names = join(unis, "name")
            return "We are cooperating with below universities that offer study on {0}: \n{1}".format(params['Subject'], uni_names)
        if params['WorkStudy'] == 'provide':
            unis = University_Course.objects.filter(offer_work_study_program = 1).values()
            uni_names = join(unis, "name")
            return "We are cooperating with below universities that offer Work Study Ptogram: \n{0}".format(uni_names)
        if params['TuitionFee'] =='lower':
            unis = University_Course.objects.filter(average_tuition_fee__gte = fuzzy_values.low_tuition_fee[0]).filter(average_tuition_fee__lte = fuzzy_values.low_tuition_fee[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having relatively cheaper tuition fees: \n{0}".format(uni_names)
        if params['TuitionFee'] =='medium':
            unis = University_Course.objects.filter(average_tuition_fee__gte = fuzzy_values.medium_tuition_fee[0]).filter(average_tuition_fee__lte = fuzzy_values.medium_tuition_fee[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having medium tuition fees: \n{0}".format(uni_names)
        if params['TuitionFee'] =='higher':
            unis = University_Course.objects.filter(average_tuition_fee__gte = fuzzy_values.high_tuition_fee[0]).filter(average_tuition_fee__lte = fuzzy_values.high_tuition_fee[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having relatively higher tuition fees: \n{0}".format(uni_names)
        if params['CostOfLiving'] =='lower':
            unis = University_Course.objects.filter(cost_of_living_index__gte = fuzzy_values.low_cost_of_living[0]).filter(cost_of_living_index__lte = fuzzy_values.low_cost_of_living[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are located in relatively cheaper cities: \n{0}".format(uni_names)
        if params['CostOfLiving'] =='medium':
            unis = University_Course.objects.filter(cost_of_living_index__gte = fuzzy_values.medium_cost_of_living[0]).filter(cost_of_living_index__lte = fuzzy_values.medium_cost_of_living[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are located in average expensive cities: \n{0}".format(uni_names)
        if params['CostOfLiving'] =='higher':
            unis = University_Course.objects.filter(cost_of_living_index__gte = fuzzy_values.high_cost_of_living[0]).filter(cost_of_living_index__lte = fuzzy_values.high_cost_of_living[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are located in relatively more expensive cities: \n{0}".format(uni_names)
        if params['AcademicRank'] =='high':
            unis = University_Course.objects.filter(academic_reputation_rank__gte = fuzzy_values.high_academic_rank[0]).filter(academic_reputation_rank__lte = fuzzy_values.high_academic_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having higher academic reputation rank: \n{0}".format(uni_names) 
        if params['AcademicRank'] =='medium':
            unis = University_Course.objects.filter(academic_reputation_rank__gte = fuzzy_values.medium_academic_rank[0]).filter(academic_reputation_rank__lte = fuzzy_values.medium_academic_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having medium academic reputation rank: \n{0}".format(uni_names) 
        if params['AcademicRank'] =='low':
            unis = University_Course.objects.filter(academic_reputation_rank__gte = fuzzy_values.low_academic_rank[0]).filter(academic_reputation_rank__lte = fuzzy_values.low_academic_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having lower academic reputation rank: \n{0}".format(uni_names)        
        if params['EmployerRank'] =='high':
            unis = University_Course.objects.filter(employer_reputation_rank__gte = fuzzy_values.high_employer_rank[0]).filter(employer_reputation_rank__lte = fuzzy_values.high_employer_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having higher employer reputation rank: \n{0}".format(uni_names) 
        if params['EmployerRank'] =='medium':
            unis = University_Course.objects.filter(employer_reputation_rank__gte = fuzzy_values.medium_employer_rank[0]).filter(employer_reputation_rank__lte = fuzzy_values.medium_employer_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having medium employer reputation rank: \n{0}".format(uni_names) 
        if params['EmployerRank'] =='low':
            unis = University_Course.objects.filter(employer_reputation_rank__gte = fuzzy_values.low_employer_rank[0]).filter(employer_reputation_rank__lte = fuzzy_values.low_employer_rank[1]).values()
            uni_names = join(unis, "name")
            return "Below universities are having lower employer reputation rank: \n{0}".format(uni_names)      

        return default_response
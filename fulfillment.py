
from Recommender.models import Student, University_Course

def join(list, attribute):
    res =""
    i =0
    while (i<len(list)):
        if i==0:
           res = list[i][attribute]
        else:
            res = res + ", " + list[i][attribute]
        i = i +1

def do_fulfillment(intent, params):
    if intent=='CityIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni: 
                    return "{0} is located in {1}".format(uni['name'], uni['city'])
        return default_response
    
    if intent=='AcademicReputationIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni: 
                    return "{0} has an academic reputation score of {1} and academic rank of {2}".format(uni['name'], uni['academic_reputation_score'], uni['academic_reputation_rank'])
        return default_response

    if intent=='EmployerReputationIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni: 
                    return "{0} has an employer reputation score of {1} and academic rank of {2}".format(uni['name'], uni['employer_reputation_score'], uni['employer_reputation_rank'])
        return default_response

    if intent=='CampusSettingIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni: 
                    return "The campus of {0} is {1}".format(uni['name'], uni['campus_setting'])
        return default_response

    if intent=='CostOfLivingIntent':
        default_response = 'I am sorry, please specify a proper city'
        if params['City']:
            unis = University_Course.objects.filter(city__icontains=params['City'][0]).values()
            for uni in unis:
                if uni: 
                    return "The cost of living index of {0} is {1}".format(uni['city'], uni['cost_of_living_index'])
        return default_response

    if intent=='GPAIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni:
                    if uni['min_GPA'] == 'no minimum':
                        return "There is no minimum GPA requirement to enroll {0}".format(uni['name'])
                    return "The minimum GPA requirement to enroll {0} is {1}".format(uni['name'], uni['min_GPA'])

        return default_response

    if intent=='IELTSIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni:
                    return "The minimum IELTS requirement to enroll {0} is {1}".format(uni['name'], uni['min_IELTS'])
        return default_response

    if intent=='TOEFLIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni:
                    return "The minimum TOEFL requirement to enroll {0} is {1}".format(uni['name'], uni['min_TOEFL'])
        return default_response

    if intent=='InternationalStudentRatioIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni:
                    return "In {0}, international student take about {1}%".format(uni['name'], 100*uni['international_student_percentage'])
        return default_response

    if intent=='TuitionFeeIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            for uni in unis:
                if uni:
                    return "The average tuition fee of {0} is {1} USD".format(uni['name'], uni['average_tuition_fee'])
        return default_response

    if intent=='WorkStudyIntent':
        default_response = 'I am sorry, please specify a proper university'
        if params['UniversityName']:
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
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
            unis = University_Course.objects.filter(name__icontains=params['UniversityName'][0]).values()
            fields = join(unis, "field_of_study")
            return "{0} offers below fields of study: {1}".format(params['UniversityName'][0], fields)
        return default_response


    if intent=='UniversityIntent':
        default_response = 'I am sorry, but I do not understand your question. Please try again'
        if params['Country']:
            unis = University_Course.objects.filter(country__icontains=params['Country'][0]).values()
            uni_names = join(unis, "name")
            return "In {0}, we are cooperating with below universities: {1}".format(params['Country'][0], uni_names)
        if params['Subject']:
            unis = University_Course.objects.filter(subject__icontains=params['Subject'][0]).values()
            uni_names = join(unis, "name")
            return "We are cooperating with below universities that offer study on {0}: {1}".format(params['Subject'][0], uni_names)
        if params['WorkStudy']:
            filters = University_Course.objects.filter(offer_work_study_program = 1)
            if params['Country']:
                filters = filters.filter(country__icontains=params['Country'][0])
            unis = filters.values()
            uni_names = join(unis, "name")
            return "In {0}, we are cooperating with below universities that offer study on {1}: {2}".format(params['Country'][0], params['Subject'][0], uni_names)
        return default_response
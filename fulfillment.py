
from Recommender.models import Student, University_Course


def do_fulfillment(intent, params):
    if intent=='CityIntent':

        default_response = 'I am sorry, please specify a proper university'

        if params['UniversityName']:
            unis = University_Course.objects.filter(name=params['UniversityName']).values()
            for uni in unis:
                if uni: 
                    return uni['city']
        return default_response
        


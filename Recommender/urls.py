from django.urls import path
from .views import university_list, recommendation
urlpatterns = [
    path('university_list/', university_list),
    path('recommendation/', recommendation),
]
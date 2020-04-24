from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('recommend/', views.load_regions, name="recommend"),
    path("countrys/", views.load_countrys, name="countrys"),
    path("result/", views.result, name="result"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('sendChat/', views.chat, name="sendChat"),
    path('university_list/', views.university_list),
    path('recommendation/', views.recommendation),
    path('chat/', views.chat)
]
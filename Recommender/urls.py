from django.urls import path

from .views import university_list, recommendation, chat

urlpatterns = [
    path('', views.index),
    path('recommend/', views.load_regions, name="recommend"),
    path("countrys/", views.load_countrys, name="countrys"),
    path("result/", views.result, name="result"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('sendChat/', views.chat, name="sendChat"),
    path('university_list/', university_list),
    path('recommendation/', recommendation),
    path('chat/', chat)
]
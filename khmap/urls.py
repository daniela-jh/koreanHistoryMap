from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.map_main, name='map_main'),
    path('quiz/', views.quiz_list, name='quiz_list'),
    path('quiz/type1/', views.quiz_type1, name='quiz_type1')
]
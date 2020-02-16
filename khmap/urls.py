from django.urls import path, include
from . import views

urlpatterns = {
    path('', views.map_main, name='map_main')
}
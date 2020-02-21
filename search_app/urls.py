from django.urls import path, include
from . import views

app_name = 'search_app'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),
]
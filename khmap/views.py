from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import Content

def map_main(request):
    contents = Content.objects.values_list()
    return render(request, 'khmap/map_main.html', {'contents': contents})
from django.shortcuts import render
from .models import Content

def map_main(request):
    return render(request, 'khmap/map_main.html', {})

def content_all(request):
    contents = Content.objects.values_list()
    return render(request, 'khmap/map_main.html', {'contents': contents})
from django.shortcuts import render
from django.http import JsonResponse

from .models import Content

def map_main(request):
    contents = Content.objects.all()
    print(contents)
    # json_contents = JsonResponse({'contents': list(contents)})
    return render(request, 'khmap/map_main.html', {'contents': contents})

def quiz_list(request):
    contents = Content.objects.all()
    return render(request, 'khmap/quiz_list.html', {'contents': contents})

def quiz_type1(request):
    contents = Content.objects.all()
    return render(request, 'khmap/quiz_type1.html', {'contents': contents})
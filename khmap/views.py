from django.shortcuts import render
from django.http import JsonResponse

from .models import Content

def map_main(request):
    contents = Content.objects.all()
    print(contents)
    # json_contents = JsonResponse({'contents': list(contents)})
    return render(request, 'khmap/map_main.html', {'contents': contents})
from django.shortcuts import render
from django.db.models import F

from .models import Content

contents = Content.objects.all()

def map_main(request):
    contents = Content.objects.all()
    print(contents)
    # json_contents = JsonResponse({'contents': list(contents)})
    return render(request, 'khmap/map_main.html', {'contents': contents})

def quiz_list(request):
    contents = Content.objects.all()
    return render(request, 'khmap/quiz_list.html', {'contents': contents})

def quiz_type1(request):
    randomQuiz = Content.objects.order_by("?").first()
    randomAnswer = Content.objects.order_by("?").exclude(locationName=randomQuiz.locationName)[:3]
    answerList = list(randomAnswer)
    return render(request, 'khmap/quiz_type1.html', {'randomQuiz': randomQuiz, 'answerList': answerList})
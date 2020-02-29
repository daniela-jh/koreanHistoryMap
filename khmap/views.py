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

# def quiz_type1(request):
#     randomQuiz = Content.objects.order_by("?").first()
#     randomAnswer = Content.objects.order_by("?").exclude(locationName=randomQuiz.locationName)[:3]
#     answerList = list(randomAnswer)
#     return render(request, 'khmap/quiz_type1.html', {'randomQuiz': randomQuiz, 'answerList': answerList})

def quiz_type1_edit(request):
    randomQuiz = Content.objects.order_by("?").first()
    randomAnswer = Content.objects.order_by("?").exclude(locationName=randomQuiz.locationName)[:3]
    answerList = list(randomAnswer)
    return render(request, 'khmap/quiz_type1_edit.html', {'randomQuiz': randomQuiz, 'answerList': answerList})

def quiz_type(request):
    randomQuizOrder = Content.objects.order_by("?")
    realQuizSet = []
    i = 0
    for quiz in randomQuizOrder:
        quizAnswer = randomQuizOrder[i]
        randomAnswer = Content.objects.order_by("?").exclude(locationName=quizAnswer.locationName)[:3]
        answerList = list(randomAnswer)
        realQuizSet.append({'answer': quizAnswer.locationName, 'option1':answerList[0].locationName, 'option2':answerList[1].locationName, 'option3':answerList[2].locationName,
                            'text1': quizAnswer.locationText1, 'text2': quizAnswer.locationText2, 'text3': quizAnswer.locationText3, 'text4': quizAnswer.locationText4})
        i = i+1
    return render(request, 'khmap/quiz_type1.html', {'realQuizSet': realQuizSet, 'randomQuizOrder': randomQuizOrder})
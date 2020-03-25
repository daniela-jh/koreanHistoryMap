from django.shortcuts import render
from django.db.models import F
import random

from .models import Content

contents = Content.objects.all()

def map_main(request):
    contents = Content.objects.all()
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

# def quiz_type1_edit(request):
#     randomQuiz = Content.objects.order_by("?").first()
#     randomAnswer = Content.objects.order_by("?").exclude(locationName=randomQuiz.locationName)[:3]
#     answerList = list(randomAnswer)
#     return render(request, 'khmap/quiz_type1_edit.html', {'randomQuiz': randomQuiz, 'answerList': answerList})

def quiz_type1(request):
    randomQuizOrder = Content.objects.order_by("?")
    realQuizSet = []
    i = 0
    for quiz in randomQuizOrder:
        quizAnswer = randomQuizOrder[i]
        randomAnswer = Content.objects.order_by("?").exclude(locationName=quizAnswer.locationName)[:3]
        answerList = list(randomAnswer)
        realQuizSet.append({'answer': quizAnswer.locationName, 'option1':answerList[0].locationName,
                            'option2':answerList[1].locationName, 'option3':answerList[2].locationName,
                            'text1': quizAnswer.locationText1, 'text2': quizAnswer.locationText2,
                            'text3': quizAnswer.locationText3, 'text4': quizAnswer.locationText4})
        i = i+1
    return render(request, 'khmap/quiz_type1.html', {'realQuizSet': realQuizSet, 'randomQuizOrder': randomQuizOrder})

def quiz_type2(request):
    randomQuizOrder = Content.objects.order_by("?")
    realQuizSet2 = []
    i = 0
    for quiz in randomQuizOrder:
        quizAnswer = randomQuizOrder[i]
        wrongOption = Content.objects.order_by("?").exclude(locationName=quizAnswer.locationName).first()
        wrongOptionList = [wrongOption.locationText1, wrongOption.locationText2,
                           wrongOption.locationText3, wrongOption.locationText4]
        wrongOptionList = [elem for elem in wrongOptionList if elem != '-']
        wrongAnswer = random.choice(wrongOptionList)
        realQuizSet2.append({'answerLocation': quizAnswer.locationName, 'wrongLocation': wrongOption.locationName,
                             'option1': quizAnswer.locationText1, 'option2': quizAnswer.locationText2,
                             'option3': quizAnswer.locationText3, 'option4': quizAnswer.locationText4,
                             'wrongAnswer': wrongAnswer})
        i = i+1
    return render(request, 'khmap/quiz_type2.html', {'realQuizSet2': realQuizSet2})
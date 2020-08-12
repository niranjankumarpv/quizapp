from django.shortcuts import render, redirect
from django.http import HttpResponse
from quizapp.models import Question
from django.contrib.auth import authenticate

''' In views.py we write a bussiness logic where it contains what the app should do.
    how to call these functions, which are in views.py ??
    So every application contains a file called urls.py , 
    hence will be able to call this specific app in the project. '''

#adding some comment to test

# Create your views here.
#Controller(MVC) -- Bussiness Logic

''' Every function generally first argument takes as request, 
    so what ever the user request GET,POST here you will get 
    as part of the request by default '''
def index(request):
    questions_list = Question.objects.all()
    return render(request, "quizapp/index.html", {'questions_list': questions_list})

def detail(request, question_id):
    message = ""
    is_correct = False
    score = 0
    if request.method == "POST":
        answer_id = int(request.POST.get("answer"))
        question = Question.objects.get(id=question_id)
        for answer in question.answer_set.all():
            if answer.id == answer_id and answer.correct:
                message = "correct answer"
                is_correct = True
                score += 1
                break
        if not is_correct:
            message = "wrong answer"

    question = Question.objects.get(id=question_id)
    return render(request, "quizapp/detail.html", {'question': question, 'message': message,
                                                   'result': is_correct, 'score': score})

def login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            return redirect('index')
        else:
            message = "Either Username or Password is wrong"
    return render(request, "quizapp/login.html", {'message': message})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from quizapp.models import Question
from . forms import QuestionForm
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
    if request.method == "POST":
        answer_id = int(request.POST.get("answer"))
        question = Question.objects.get(id=question_id)
        for answer in question.answer_set.all():
            if answer.id == answer_id and answer.correct:
                message = "correct answer"
                is_correct = True
                item = Question.objects.get(pk=question_id)
                item.points = 1
                item.save()
                break
        if not is_correct:
            item = Question.objects.get(pk=question_id)
            item.points = 0
            item.save()
            message = "wrong answer"
    question = Question.objects.get(id=question_id)
    return render(request, "quizapp/detail.html", {'question': question, 'message': message,
                                                   'result': is_correct})

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

def point(request):
    total_points = 0
    if request.method == "POST":
        form = QuestionForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Question.objects.all
            for item in all_items:
                total_points = total_points + item.points
            return render(request, "quizapp/point.html", {'all_items': all_items, 'total_point':total_points})
    else:
        items = Question.objects.all()
        for item in items:
            total_points = total_points + item.points
        all_items = Question.objects.all
        return render(request, "quizapp/point.html", {'all_items': all_items, 'total_points':total_points})
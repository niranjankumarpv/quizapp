from django.shortcuts import render
from django.http import HttpResponse
from quizapp.models import Question

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
    # output = ""
    # for question i n question:
    #     output = output + question.content
    #return HttpResponse(output)
    return render(request, "quizapp/index.html", {'questions_list': questions_list})

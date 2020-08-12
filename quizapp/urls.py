from django.urls import path
from . import views

#Create a list "urlpatterns" what should happen
#Here when there is no path at the end of the URL it will views.index()
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('login', views.login, name='login')
]

#Hence after creating the URL patterns in the urls.py of the application, we have to include it in the urls.py of the project.

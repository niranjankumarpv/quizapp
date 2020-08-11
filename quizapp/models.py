from django.db import models

''' 
    models.py --> models is a place where we define
    Whatever you define a class in a model representing a table in your DB. 
    This is called as ORM -> Object Relational Model.
    Here when you define a class django will automatically create a table - Don't give plural class name 
    as the django will create a table name in plural form
'''
class Question(models.Model):
    content = models.CharField(blank=False, max_length=200, help_text="Enter the Question")

    def  __str__(self):
        return self.content

class Answer(models.Model):
    content = models.CharField(max_length=100)
    correct = models.BooleanField(default=False, blank=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
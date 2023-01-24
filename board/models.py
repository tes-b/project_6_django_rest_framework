from django.db import models
from django.contrib.auth.models import User
# sql table에 저장되는 양식

class Question(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

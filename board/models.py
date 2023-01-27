from django.db import models
from django.contrib.auth.models import User
from test_web.settings import AUTH_USER_MODEL
# sql table에 저장되는 양식

class Question(models.Model):
    # author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    # author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

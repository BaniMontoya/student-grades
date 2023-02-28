from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    address = models.CharField(max_length=100, default="unknow")
    whatsapp = models.CharField(max_length=20, default="unknow")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.answer_text

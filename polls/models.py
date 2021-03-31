from django.db import models
import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

#class Employee(models.Model):
#    username = models.CharField(max_length=200)
#    email = models.CharField(max_length=200)
#
#    def __str__(self):
#        return self.username


class Vacation(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200,null=False)
    date_from = models.DateField(auto_now_add=False, auto_now=False, null=False)
    date_to = models.DateField(auto_now_add=False, auto_now=False, null= False)

    def __str__(self):
        return self.description


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

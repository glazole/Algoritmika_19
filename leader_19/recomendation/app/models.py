from django.db import models
from django.contrib.auth.models import AbstractUser


class UserId(AbstractUser): 
    added_at = models.CharField(max_length=255) #дата создание личного дела 
    birth_date = models.DateField() # дата рождения
    sex = models.CharField(max_length=10) 
    address = models.CharField(max_length=255)  
   # is_banned = models.BooleanField(default=False)
  

class Profile(models.Model):
    username = models.IntegerField(default=0)
    test_result = models.IntegerField(default=0)

    objects = models.Manager()
 
    def __str__(self):
            return self.id


class Question(models.Model):
    question_text = models.CharField(max_length = 255, default=0)
    objects = models.Manager()

    def __str__(self):
            return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 255)
    votes = models.IntegerField(default = 0)

    objects = models.Manager()

    def __str__(self):
            return self.choice_text


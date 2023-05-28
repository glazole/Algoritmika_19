from django import forms
from django.forms import ModelForm
from .models import UserId, Choice, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

class UserIdCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserId
        fields = ('username', 'added_at', 'sex', 'address', 'birth_date')

class UserIdChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserId
        fields = ('username', 'added_at', 'sex', 'address','birth_date')


class AnswerForm(forms.Form):
    username = forms.CharField(max_length=64)
    test_result = forms.CharField()
    
 #   def clean(self, *args, **kwargs):
  #      username = self.cleaned_data['username']
   #     try:
    #        user = UserId.objects.get(username=username)
     #   except User.DoesNotExist:
      #      raise forms.ValidationError('Такого пользователя не существует') 
       # return super(AnswerForm, self).clean(*args, **kwargs)

    def save(self):
        profile = Profile.objects.create(**self.cleaned_data)
        profile.save()
        return profile


 

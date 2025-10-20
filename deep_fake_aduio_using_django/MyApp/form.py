from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video

class RegistrationForm(UserCreationForm):
      class Meta:
            model=User
            fields=('username','email','first_name','last_name')
          
              
class Video_form(forms.ModelForm):
      class Meta:
            model=Video
            fields=("video",)
             
          
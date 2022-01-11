from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import project

class PostForm(ModelForm):
    
    class meta:
        model = project
        fields = '__all__'
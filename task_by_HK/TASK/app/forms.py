from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','mob']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user_detail','task_detail','task_type']
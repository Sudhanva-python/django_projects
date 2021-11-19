from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    desc = forms.CharField(max_length=250,widget=forms.Textarea)
    

    class Meta :
        model = Task
        fields = ['name','desc']

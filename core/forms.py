from django import forms
from core.models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':15,'class':'form-control'}))

    class Meta:
        model = Task
        fields = ['title','description','completed']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

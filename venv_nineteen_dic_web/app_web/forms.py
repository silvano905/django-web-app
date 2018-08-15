from django import forms
from django.contrib.auth.models import User
from .models import MakeWord


class FirstForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class TranslateForm(forms.Form):
    text = forms.CharField(max_length=20, label='Search ')


class CreateForm(forms.ModelForm):
    class Meta:
        model = MakeWord
        fields = '__all__'
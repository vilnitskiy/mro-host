from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

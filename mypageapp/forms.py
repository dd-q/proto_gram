from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = ['name', 'email','phone','address']
        labels = {'name':'이름', 'email':'이메일','phone':'연락처','address':'주소'}
        exclude = ['profile_photo']
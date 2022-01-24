from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email','user_phone','user_addr']
        labels = {'user_name':'이름', 'email':'이메일','user_phone':'연락처','addr':'주소'}
        exclude = ['profile_img']


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        # labels = {}

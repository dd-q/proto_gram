from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {'user_name':'이름', 'email':'이메일','user_phone':'연락처','user_addr':'주소', 'profile_img':'프사'}
        # exclude = []


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        # labels = {}

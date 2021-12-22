from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

UserModel = get_user_model()


class UserUpdateModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

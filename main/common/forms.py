from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    # 중대 & 휴대폰 번호 field 가 추가 되어야함.
    # login시 인증기능도 추가 되어야 함.
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


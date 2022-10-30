from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2', 'age', 'address', 'brithday', 'user_image' ]
        labels = {
            'username' : '아이디',
            'password1' : '비밀번호',
            'password2' : '비밀번호 확인',
            'age' : '나이',
            'address' : '주소',
            'brithday' : '생년월일',
            'user_image': '사진첨부'
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['user_image']
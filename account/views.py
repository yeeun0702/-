from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from account.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('mypage')
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})


def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('write')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('main')

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from account.forms import CustomUserCreationForm
from .forms import CustomUser

################################# 비밀번호 변경
def update_password(request) :
    if request.method == "POST" :
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid() :
            user = form.save() # 이때 로그아웃처리됨. session 정보 날라가고, 로그인정보도 사라짐
            update_session_auth_hash(request, user) # session 을 update 이렇게 해야 비밀번호를 바꾸더라도 로그아웃이 되지 않음
            return redirect('main')
    else :
        form = PasswordChangeForm(request.user)
    return render(request, 'update_password.html',{'form':form})



#마이페이지
def mypage(request):
    image = request.user.user_image
    return render(request, 'mypage.html', {'image':image})

#프로필 이미지 수정
def mypage_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            image = request.user.user_image
            return render(request, 'mypage.html', {'image':image})
    else:
        form = CustomUserChangeForm(instance=request.user)
        image = request.user.user_image
        return render(request, 'mypage_edit.html', {
            'form':form,
            'image':image})


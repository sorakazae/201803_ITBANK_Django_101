from django.shortcuts import render
from django.contrib.auth.models import User #장고에서 만든 User모델 클래스
from . import forms
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate #login(),logout() 로그인, 로그아웃 함수
from user.forms import loginForm
# Create your views here.

def sign(request):
    if request.method == "POST": #post로 접근
        form = forms.signForm(request.POST) #사용자 입력을 signForm에 입력
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data) # 새로운 유저 생성
            return HttpResponseRedirect(reverse('user:login'))
    else: #get으로 접근
        form = forms.signForm()
        
    return render(request, 'registration/sign.html', {'form':form})

#login 기능, logout 기능
def clogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #잘못된 아이디, 비밀번호를 입력하면 user에 None이 반환
        user = authenticate(username=username,password=password) #유효한 아이디,비번인지 확인
        if user is not None: #유효한 사용자 인가?
            login(request,user)#현재 접속한 request에 user로 접속시킴
            return HttpResponseRedirect(reverse('index'))
        else:
            form = loginForm(request.POST)
            error_log = "로그인 실패. 아이디나 비밀번호가 틀렸습니다"
            return render(request, 'registration/login.html',{'form': form, 'error_log':error_log})
    else:
        form = loginForm()
    return render(request, 'registration/login.html',{'form' : form})
def clogout(request):
    logout(request)
    return HttpResponseRedirect(reverse ('user:login'))
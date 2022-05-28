from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    #POST 요청 -> 로그인 처리
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        user = auth.authenticate(request, username= username, password= password) #등록된 user라면 user객체 반환   
        if user is not None: #등록된 user라면
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    #GET 요청 -> login form을 담고있는 login.html을 띄워줌
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    return




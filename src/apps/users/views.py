from django.shortcuts import render
from django.contrib.auth import logout

def login(request):
    return render(request, 'users/registration/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/registration/logged_out.html', {'logout_message': "ログアウトしました。"})

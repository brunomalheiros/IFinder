from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout
def cadastro(request):
  

def login(request):


def logout_view(request):
    logout(request)
    return redirect('home')



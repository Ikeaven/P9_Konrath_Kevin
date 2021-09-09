from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse


def index(request):
    return render(request, 'accueil/index.html')

def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if not user.exists():
            user = User.objects.create(
                username = username,
                password = make_password(password, 'salt', 'default')
            )
            redirect('accueil')
        else:
            print("user already exist")
            redirect('accueil')
    else:
        return render(request, 'accueil/inscription.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        user = User.objects.filter(username=username)
        if not user.exists():
            return redirect("inscription")

        return redirect('flux')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import InscriptionForm


def index(request):
    return render(request, 'accueil/index.html')

# def inscription(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = User.objects.filter(username=username)
#         if not user.exists():
#             user = User.objects.create(
#                 username = username,
#                 password = make_password(password, 'salt', 'default')
#             )
#             return redirect('accueil')
#         else:
#             print("user already exist")
#             return redirect('accueil')

#     else:
#         return render(request, 'accueil/inscription.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = User.objects.filter(username=username)
            if not user.exists():
                user = User.objects.create(
                    username = username,
                    password = make_password(password, 'salt', 'default')
                )
            else:
                print("user already exist")

            return redirect('accueil')
        else:
            return render(request, 'accueil/inscription.html', {'form': form})
    else:
        form = InscriptionForm()
    return render(request, 'accueil/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('flux')
        else:
            return redirect('accueil')
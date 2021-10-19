from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import DivErrorList, InscriptionForm


def index(request):
    context = {"error": False}
    return render(request, 'accueil/index.html', context)


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            verify_password = request.POST.get('verify_password')

            if password != verify_password:
                form.add_error('verify_password', "Les deux mots de passe ne sont pas identiques !")
                return render(request, 'accueil/inscription.html', {'form': form})
            else:
                user = User.objects.filter(username=username)
                if not user.exists():
                    user = User.objects.create(
                        username = username,
                        password = make_password(password, 'salt', 'default')
                    )
                    return redirect('accueil')
                else:
                    form.add_error('username', "Ce nom d'utilisateur est déjà utilisé")
                    return render(request, 'accueil/inscription.html', {'form': form})

        else:
            return render(request, 'accueil/inscription.html', {'form': form})
    else:
        form = InscriptionForm(error_class=DivErrorList)
    return render(request, 'accueil/inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('flux')
        else:
            context = {'error':True}
            return render(request, 'accueil/index.html', context)
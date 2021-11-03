from django.urls import path
# from django.urls.resolvers import URLPattern

from . import views

# app_name = 'accueil'
urlpatterns = [
    path('', views.index, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
]

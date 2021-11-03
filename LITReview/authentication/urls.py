from django.urls import path
# from django.urls.resolvers import URLPattern

from . import views

# app_name = 'authentication'
urlpatterns = [
    path('', views.index, name='authentication'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
]

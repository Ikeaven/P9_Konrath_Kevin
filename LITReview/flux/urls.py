from django.urls import path
# from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [path('', views.index, name='flux'),
path('logout_view', views.logout_view, name='logout'),
path('create_ticket', views.create_ticket, name='create_ticket' )
]
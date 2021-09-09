from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Ticket


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets' : tickets}
    return render(request, 'flux/index.html', context)
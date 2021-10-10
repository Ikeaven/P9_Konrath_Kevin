from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
# from django.http import HttpResponse
# Create your views here.
from .models import Ticket, Review, UserFollows
from .forms import CritiqueRequestForm, ReviewForm, AbonnementsForm
from django.core.files.storage import default_storage
from django.views import generic


@login_required
def index(request):
    tickets = Ticket.objects.order_by('-time_created')
    reviews = Review.objects.all()
    context = {'tickets' : tickets, 'reviews' : reviews}
    return render(request, 'flux/index.html', context)

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CritiqueRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]

            ticket = Ticket.objects.create(
                title = title,
                description = description,
                image = image,
                user = request.user
            )

        return redirect('flux')

    form = CritiqueRequestForm()
    context = {'form': form}
    return render(request, 'flux/create_ticket.html', context)

@login_required
def create_review(request, ticket_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        # if form.is_valid():
        review = Review.objects.create(
            ticket = Ticket.objects.get(pk = ticket_id),
            rating = request.POST['rating'],
            user = request.user,
            headline = request.POST["headline"],
            body = request.POST["body"]
            )


        # else:
        #     print('invalid data')
        return redirect('flux')

    ticket = Ticket.objects.get(pk = ticket_id)
    form = ReviewForm()
    context = {'ticket' : ticket, 'form' : form}
    return render(request, 'flux/create_review.html', context)

# @login_required
# def posts(request):
#     return render(request, 'flux/posts.html')

class TicketsListView(generic.ListView):
    template_name = 'flux/posts_list.html'
    model = Ticket

    def get(self, request):
        tickets = Ticket.objects.filter(user = request.user.id)
        reviews = Review.objects.filter(user = request.user.id)
        related_ticket = []
        context = {'tickets': tickets, 'reviews':reviews}
        return render(request, self.template_name, context)

class TicketDetailView(generic.UpdateView):
    model = Ticket
    template_name='flux/detail_ticket.html'
    form_class = CritiqueRequestForm
    success_url = '/flux/posts'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class TicketDeleteView(generic.DeleteView):
    model = Ticket
    success_url = ('/flux/posts')

class ReviewDeleteView(generic.DeleteView):
    model = Review
    success_url = ('/flux/posts')

@login_required
def abonnements(request):
    if request.method == 'POST':
        # form = AbonnementsForm(request.POST)
        name = request.POST['name']
        try:
            user = get_object_or_404(User, username=name)
            UserFollows.objects.create(
                user = request.user,
                followed_user = user,
            )
        except User.DoesNotExist:
            raise Http404("No MyModel matches the given query.")


    form = AbonnementsForm
    followed_users = UserFollows.objects.filter(user = request.user.id)
    followers = UserFollows.objects.filter(followed_user = request.user.id)
    context = {'form':form, 'followed_users':followed_users, 'followers':followers}
    return render(request, 'flux/abonnements.html', context)

class UnsubscribeView(generic.DeleteView):
    model = UserFollows
    success_url = ('/flux/abonnements')

def logout_view(request):
    logout(request)
    return redirect('accueil')
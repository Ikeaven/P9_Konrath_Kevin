from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.query import EmptyQuerySet
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from accueil.models import User
from .models import Ticket, Review, UserFollows
from django.db.models import CharField, Value, Count
from .forms import CritiqueRequestForm, ReviewForm, AbonnementsForm, ReviewRequestForm
from django.core.files.storage import default_storage
from django.views import generic
from itertools import chain


def get_users_viewable_reviews(user):
    followed_users = UserFollows.objects.filter(user = user)
    tickets = Ticket.objects.filter(user = user)
    reviews = Review.objects.filter(user = user) | Review.objects.filter(user__in = [el.followed_user for el in followed_users]) | Review.objects.filter(ticket__in = tickets)
    return reviews

def get_users_viewable_tickets(user):
    followed_users = UserFollows.objects.filter(user = user)

    tickets = Ticket.objects.filter(user = user) | Ticket.objects.filter(user__in = [el.followed_user for el in followed_users])
    return tickets

@login_required
def index(request):
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    tickets = tickets.annotate(num_reviews = Count('review') )

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    context = {'posts':posts, 'current_page':'flux'}
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


@login_required
def create_ticket_and_review(request):
    ticket_form = CritiqueRequestForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        ticket_form = CritiqueRequestForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = Ticket.objects.create(
                title = ticket_form.cleaned_data['title'],
                description = ticket_form.cleaned_data['description'],
                image = ticket_form.cleaned_data['image'],
                user = request.user
            )
            Review.objects.create(
            ticket = Ticket.objects.get(pk = ticket.id),
            rating = review_form.cleaned_data['rating'],
            user = request.user,
            headline = review_form.cleaned_data['headline'],
            body = review_form.cleaned_data['body']
            )
            return redirect('flux')
        return redirect('create_ticket_and_review')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'flux/create_ticket_and_review.html', context=context)



class TicketsListView(LoginRequiredMixin,generic.ListView):
    template_name = 'flux/posts_list.html'
    model = Ticket

    def get(self, request):
        tickets = Ticket.objects.filter(user = request.user.id)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        reviews = Review.objects.filter(user = request.user.id)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
        )
        context = {'posts':posts, 'current_page':'posts'}
        return render(request, self.template_name, context)

class TicketDetailView(LoginRequiredMixin, generic.UpdateView):
    model = Ticket
    template_name = 'flux/detail_ticket.html'
    form_class = CritiqueRequestForm
    success_url = '/flux/posts'

    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        if request.user == ticket.user:
            return super().get(self, request, pk)
        else :
            raise PermissionDenied

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)


class ReviewDetailView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    template_name = 'flux/detail_review.html'
    form_class = ReviewRequestForm
    success_url = '/flux/posts'

    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.user == review.user:
            return super().get(self, request, pk)
        else :
            raise PermissionDenied

    # def form_valid(self, form):
    #     return super().form_valid(form)

class TicketDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ticket
    success_url = ('/flux/posts')

    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        if request.user == ticket.user:
            return super().get(self, request, pk)
        else :
            raise PermissionDenied


class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    success_url = ('/flux/posts')

    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.user == review.user:
            return super().get(self, request, pk)
        else :
            raise PermissionDenied


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
    context = {'form':form, 'followed_users':followed_users, 'followers':followers, 'current_page':'abonnements'}
    return render(request, 'flux/abonnements.html', context)

class UnsubscribeView(LoginRequiredMixin, generic.DeleteView):
    model = UserFollows
    success_url = ('/flux/abonnements')

def logout_view(request):
    logout(request)
    return redirect('accueil')
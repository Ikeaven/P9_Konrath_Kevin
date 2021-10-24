from django.urls import path
# from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='flux'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('create_ticket', views.create_ticket, name='create_ticket'),
    path('create_review/<int:ticket_id>', views.create_review, name='create_review'),
    path('create_ticket_and_review', views.create_ticket_and_review, name='create_ticket_and_review'),
    path('posts', views.TicketsListView.as_view(), name='posts'),
    path('abonnements', views.abonnements, name='abonnements'),
    path('modify_ticket/<int:pk>', views.TicketDetailView.as_view(), name='tickets_details'),
    path('modify_review/<int:pk>', views.ReviewDetailView.as_view(), name='review_details'),
    path('delete_ticket/<int:pk>', views.TicketDeleteView.as_view(), name='delete_ticket'),
    path('delete_review/<int:pk>', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('unsubscribe/<int:pk>', views.UnsubscribeView.as_view(), name='unsubscribe')
]

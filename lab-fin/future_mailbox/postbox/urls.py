from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    EventListView, EventDetailView, EventCreateView,
    EventUpdateView, EventDeleteView, signup_view, my_events,UserEventsView,
) 

app_name = 'postbox'

urlpatterns = [
  
  path('timeline/', EventListView.as_view(), name='timeline'),

   path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),

    # Event CRUD
    path('event/add/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    # My Events


    path('timeline/react/<int:event_id>/', views.react_event, name='react_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('messages/compose/', views.compose_message, name='compose_message'),
    path('user/<str:username>/events/', UserEventsView.as_view(), name='user_events'),

    # Authentication
    path('signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='postbox/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='postbox:login'), name='logout'),
]

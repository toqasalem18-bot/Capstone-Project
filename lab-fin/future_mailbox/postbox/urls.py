from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    EventListView, EventDetailView, EventCreateView,
    EventUpdateView, EventDeleteView, signup_view,
    my_events, user_events, 
)
from .views import FutureEventListView, future_events

app_name = 'postbox'

urlpatterns = [
    # Timeline (Past & Today)
    path('timeline/', EventListView.as_view(), name='timeline'),

    # Future Events
    path('future/', FutureEventListView.as_view(), name='future_events_view'),  
    path('future-events/', future_events, name='future_events_func'),           

    # Comments
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    # Event Detail
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),

    # Event CRUD
    path('event/add/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    # Reactions
    path('timeline/react/<int:event_id>/', views.react_event, name='react_event'),

    # My Events
    path('my-events/', my_events, name='my_events'),

    # User Events
    path('user/<str:username>/events/', user_events, name='user_events'),

    # Authentication
    path('signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='postbox/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='postbox:login'), name='logout'),
]

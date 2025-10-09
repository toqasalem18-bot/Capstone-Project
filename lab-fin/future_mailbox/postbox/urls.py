from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EventListView, EventDetailView, EventCreateView,
    EventUpdateView, EventDeleteView, signup_view, my_events ,add_comment
)

app_name = 'postbox'

urlpatterns = [
    path('timeline/', EventListView.as_view(), name='timeline'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/add/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('my-events/', my_events, name='my_events'),
    path('signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='postbox/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='postbox:login'), name='logout'),
    path('event/<int:event_id>/add-comment/', add_comment, name='add_comment'),


]

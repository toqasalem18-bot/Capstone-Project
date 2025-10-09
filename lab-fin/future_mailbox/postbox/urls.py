from django.urls import path
from . import views

app_name = 'postbox'

urlpatterns = [
    # Dashboard والـ CRUD القديم (Message)
    #path('dashboard/', views.dashboard, name='dashboard'),

    # الأحداث الجديدة (Events)
    path('events/', views.EventListView.as_view(), name='timeline'),  # صفحة جميع الأحداث
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/create/', views.EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_edit'),
    path('my-events/', views.my_events, name='my_events'),

    # التسجيل القديم
    path('signup/', views.signup_view, name='signup'),
]

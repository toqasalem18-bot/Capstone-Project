from django.urls import path
from . import views

app_name = 'postbox'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('messages/', views.MessageListView.as_view(), name='message_list'),   
    path('signup/', views.signup_view, name='signup'),                
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),  # تفاصيل الرسالة
    path('messages/create/', views.MessageCreateView.as_view(), name='message_create'),   # إنشاء رسالة جديدة
]

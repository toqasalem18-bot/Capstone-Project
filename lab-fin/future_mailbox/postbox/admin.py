from django.contrib import admin
from .models import Event, Comment, Notification

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event_date', 'event_type', 'hearts', 'thumbs', 'tada')
    list_filter = ('event_type', 'event_date', 'user')
    search_fields = ('title', 'description', 'user__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'created_at', 'hearts')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username', 'event__title')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('message', 'recipient__username')

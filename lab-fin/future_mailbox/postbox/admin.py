from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_by', 'recipient', 'send_at', 'sent')
    list_filter = ('sent', 'send_at', 'created_by')
    search_fields = ('subject', 'body', 'recipient__username')


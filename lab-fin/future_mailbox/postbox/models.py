from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('birthday', 'Birthday'),
        ('graduation', 'Graduation'),
        ('anniversary', 'Anniversary'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    event_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    hearts = models.PositiveIntegerField(default=0)
    thumbs = models.PositiveIntegerField(default=0)
    tada = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hearts = models.PositiveIntegerField(default=0)  # ← أضفت default=0

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"


class Message(models.Model):
    subject = models.CharField(max_length=200)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    body = models.TextField()
    send_at = models.DateTimeField(blank=True, null=True)
    sent = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


from .models import Event, Comment  



class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message[:30]}"

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
   

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"

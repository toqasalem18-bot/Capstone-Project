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

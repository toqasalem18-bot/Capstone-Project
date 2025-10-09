from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    send_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Message
        fields = ['subject', 'body', 'recipient', 'send_at']  

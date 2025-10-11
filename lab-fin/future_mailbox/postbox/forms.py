from django import forms
from .models import Event, Comment
from .models import Message

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'event_type']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'write your comment here'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

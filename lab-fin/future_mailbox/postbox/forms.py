from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date']

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

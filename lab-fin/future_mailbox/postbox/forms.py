from django import forms
from .models import Event, Comment, Message

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'event_type', 'custom_event_type']
        widgets = {
            'event_type': forms.Select(attrs={'class': 'form-control', 'id': 'event_type_select'}),
            'custom_event_type': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'custom_event_type',
                'placeholder': 'Enter your event type',
                'rows': 3
            }),
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

   

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

from django.urls import reverse
from .models import Notification

def create_notification(user, event, notif_type='comment'):
    
    if notif_type == 'comment':
        message = f"{user.username} added a comment on your event '{event.title}'."
    elif notif_type == 'heart':
        message = f"{user.username} ❤️ liked your event '{event.title}'."
    elif notif_type == 'thumbs':
        message = f"{user.username} 👍 reacted to your event '{event.title}'."
    elif notif_type == 'tada':
        message = f"{user.username} 🎉 congratulated your event '{event.title}'."
    else:
        message = f"{user.username} reacted to your event '{event.title}'."

    Notification.objects.create(
        recipient=event.user,
        message=message,
        link=reverse('postbox:event_detail', args=[event.id])
    )

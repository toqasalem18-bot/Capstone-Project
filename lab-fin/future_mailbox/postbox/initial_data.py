# postbox/initial_data.py

from django.contrib.auth.models import User
from postbox.models import Event, Comment, Notification
from django.utils import timezone

def load_data():
    # ----- Users -----
    user1, created = User.objects.get_or_create(username="ahmad", email="ahmad@example.com")
    if created:
        user1.set_password("123456")  # ضع كلمة مرور آمنة حسب الحاجة
        user1.save()

    user2, created = User.objects.get_or_create(username="sara", email="sara@example.com")
    if created:
        user2.set_password("123456")
        user2.save()

    user3, created = User.objects.get_or_create(username="toqa", email="toqa@example.com")
    if created:
        user3.set_password("123456")
        user3.save()

    # ----- Events -----
    event1, _ = Event.objects.get_or_create(
        user=user1,
        created_by=user1,
        title="Ahmad's Birthday",
        description="Celebrating Ahmad's 25th birthday!",
        event_date=timezone.now() + timezone.timedelta(days=5),
        event_type="Birthday"
    )

    event2, _ = Event.objects.get_or_create(
        user=user2,
        created_by=user2,
        title="Sara's Graduation",
        description="Sara graduates from university 🎓",
        event_date=timezone.now() + timezone.timedelta(days=10),
        event_type="Graduation"
    )

    # ----- Comments -----
    Comment.objects.get_or_create(
        event=event1,
        user=user2,
        content="Happy Birthday Ahmad!",
        created_at=timezone.now()
    )

    Comment.objects.get_or_create(
        event=event2,
        user=user1,
        content="Congrats Sara! 🎉",
        created_at=timezone.now()
    )

    # ----- Notifications -----
    Notification.objects.get_or_create(
        recipient=user1,
        message="Sara commented on your event!",
        link=f"/events/{event1.id}/",
        is_read=False,
        created_at=timezone.now()
    )

    Notification.objects.get_or_create(
        recipient=user2,
        message="Ahmad commented on your event!",
        link=f"/events/{event2.id}/",
        is_read=False,
        created_at=timezone.now()
    )

    print("✅ Dummy data added successfully!")

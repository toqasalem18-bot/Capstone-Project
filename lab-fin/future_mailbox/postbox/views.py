from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

from .models import Event, Comment, Notification
from .forms import EventForm, CommentForm
from .utils import create_notification

User = get_user_model()


# ==========================
# React to Event
# ==========================
@require_POST
def react_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    reaction_type = request.POST.get('reaction')
    if reaction_type == 'heart':
        event.hearts += 1
        create_notification(request.user, event, 'heart')
    elif reaction_type == 'thumbs':
        event.thumbs += 1
        create_notification(request.user, event, 'thumbs')
    elif reaction_type == 'tada':
        event.tada += 1
        create_notification(request.user, event, 'tada')
    else:
        return JsonResponse({'error': 'Invalid reaction'}, status=400)
    event.save()
    return JsonResponse({'hearts': event.hearts, 'thumbs': event.thumbs, 'tada': event.tada})


# ==========================
# Timeline
# ==========================
class EventListView(ListView):
    model = Event
    template_name = 'postbox/timeline.html'
    context_object_name = 'event_list'
    ordering = ['-event_date', '-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['unread_count'] = self.request.user.notifications.filter(is_read=False).count()
            context['all_notifications'] = self.request.user.notifications.all().order_by('-created_at')
        else:
            context['unread_count'] = 0
            context['all_notifications'] = []
        return context


# ==========================
# Event Detail + Comments
# ==========================
@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'postbox/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.event = self.object
            comment.save()

            if comment.user != self.object.user:
                create_notification(comment.user, self.object, 'comment')

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'user': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%b %d, %Y %H:%M'),
                    'comment_id': comment.id
                })

            return redirect('postbox:event_detail', pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


# ==========================
# Edit Comment
# ==========================
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return JsonResponse({'error': 'Not allowed'}, status=403)

    if request.method == 'POST':
        content = request.POST.get('content')
        comment.content = content
        comment.save()
        return JsonResponse({'success': True, 'content': comment.content})

    return JsonResponse({'error': 'Invalid request'}, status=400)


# ==========================
# Delete Comment
# ==========================
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user and comment.event.user != request.user:
        return JsonResponse({'error': 'Not allowed'}, status=403)
    comment.delete()
    return JsonResponse({'success': True})


# ==========================
# Event Create View
# ==========================
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/event_create.html'
    success_url = reverse_lazy('postbox:timeline')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user

        custom_type = self.request.POST.get('custom_event_type')
        if form.cleaned_data.get('event_type') == 'other' and custom_type:
            event.event_type = custom_type

        if self.request.FILES.get('image'):
            event.image = self.request.FILES['image']

        event.save()

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'title': event.title,
                'description': event.description[:100] + '...',
                'event_date': event.event_date.strftime('%b %d, %Y'),
                'user': event.user.username,
                'image_url': event.image.url if event.image else '',
                'detail_url': reverse('postbox:event_detail', args=[event.id])
            })

        return super().form_valid(form)


# ==========================
# Event Update View
# ==========================
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/event_form.html'
    success_url = reverse_lazy('postbox:timeline')

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def form_valid(self, form):
        event = form.save(commit=False)
        if not event.user:
            event.user = self.request.user

        if self.request.POST.get('remove_image') == '1':
            event.image.delete(save=False)
            event.image = None

        event.save()
        return super().form_valid(form)


# ==========================
# Event Delete View
# ==========================
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'postbox/event_confirm_delete.html'
    success_url = reverse_lazy('postbox:timeline')

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


# ==========================
# Signup
# ==========================
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('postbox:timeline')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('postbox:timeline')
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'postbox/signup.html', {'form': form})


# ==========================
# My Events
# ==========================
@login_required
def my_events(request):
    event_list = Event.objects.filter(user=request.user).order_by('-event_date')
    return render(request, 'postbox/my_events.html', {'event_list': event_list})


# ==========================
# Notifications
# ==========================
@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'postbox/notifications.html', {'notifications': notifications})


# ==========================
# User Events
# ==========================
@login_required
def user_events(request, username):
    user = get_object_or_404(User, username=username)
    events = Event.objects.filter(user=user).order_by('-event_date', '-created_at')
    return render(request, 'postbox/user_events.html', {'user': user, 'events': events})

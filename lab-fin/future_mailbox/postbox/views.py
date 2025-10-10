from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Event, Comment
from .forms import EventForm, CommentForm

from .models import Message  
from .forms import MessageForm     

@login_required(login_url='/accounts/login/')
def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.created_by = request.user
            message.save()
            return redirect('postbox:timeline')  
    else:
        form = MessageForm()

  
    events = Event.objects.filter(user=request.user)

    return render(request, 'postbox/message_form.html', {'form': form, 'events': events})




from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
@require_POST
def react_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    reaction_type = request.POST.get('reaction')

    if reaction_type == 'heart':
        event.hearts += 1
    elif reaction_type == 'thumbs':
        event.thumbs += 1
    elif reaction_type == 'tada':
        event.tada += 1
    else:
        return JsonResponse({'error': 'Invalid reaction'}, status=400)

    event.save()
    return JsonResponse({
        'hearts': event.hearts,
        'thumbs': event.thumbs,
        'tada': event.tada
    })

# ==========================
# Timeline 
# ==========================
class EventListView(ListView):
    model = Event
    template_name = 'postbox/timeline.html'
    context_object_name = 'event_list'  
    ordering = ['-event_date', '-created_at']   


# ==========================
# Event Detail + Comments
# ==========================
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
            return redirect('postbox:event_detail', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

# ==========================
# Event Create
# ==========================
from django.http import JsonResponse
from django.urls import reverse

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

        event.save()

        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'title': event.title,
                'description': event.description[:100] + '...',
                'event_date': event.event_date.strftime('%b %d, %Y'),
                'user': event.user.username,
                'detail_url': reverse('postbox:event_detail', args=[event.id])
            })

        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
        return super().form_invalid(form)

# ==========================
# Event Update
# ==========================
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/event_form.html'
    success_url = reverse_lazy('postbox:timeline')

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

# ==========================
# Event Delete
# ==========================
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'postbox/event_confirm_delete.html'
    success_url = reverse_lazy('postbox:timeline')

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

# ==========================
# Signup / Registration
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
# My Events (User's own events)
# ==========================
@login_required(login_url='/accounts/login/')
def my_events(request):
    events = Event.objects.filter(user=request.user).order_by('-event_date')
    return render(request, 'postbox/my_events.html', {'events': events})

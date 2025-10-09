from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.contrib.auth.decorators import login_required

# ==========================
# قائمة الأحداث - Timeline
# ==========================
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'postbox/timeline.html'
    context_object_name = 'events'
    ordering = ['-event_date']

# ==========================
# تفاصيل الحدث + التعليقات
# ==========================
class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'postbox/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
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
        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)

# ==========================
# إنشاء حدث جديد
# ==========================
from django.urls import reverse_lazy

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/event_create.html'
    success_url = reverse_lazy('postbox:timeline')  # هنا بدل 'dashboard'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/evente_form.html'
    success_url = reverse_lazy('postbox:timeline')  # هنا بدل 'dashboard'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

# ==========================
#  صفحة التسجيل (Sign up)
# ==========================
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('postbox:timeline')  # إذا مسجل دخول مسبقًا

    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('postbox:timeline')  # بعد التسجيل، أرسل للتايم لاين
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'postbox/signup.html', {'form': form})

# ==========================
# صفحة "My Events" لكل مستخدم
# ==========================
@login_required(login_url='/accounts/login/')
def my_events(request):
    events = Event.objects.filter(user=request.user).order_by('-event_date')
    return render(request, 'postbox/my_events.html', {'events': events})

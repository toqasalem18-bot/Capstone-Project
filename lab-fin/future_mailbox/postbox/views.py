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
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/event_create.html'
    success_url = reverse_lazy('postbox:timeline')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return super().form_valid(form)

# ==========================
# تعديل حدث
# ==========================
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'postbox/evente_form.html'
    success_url = reverse_lazy('postbox:timeline')

    def get_queryset(self):
        # المستخدم يمكنه تعديل أحداثه فقط
        return Event.objects.filter(user=self.request.user)


# ==========================
#  صفحة التسجيل (Sign up)
# ==========================
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('postbox:dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, "   the user alaready here  😅")
        elif form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('postbox:dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'postbox/signup.html', {'form': form})

# ==========================
#  لوحة التحكم (Dashboard)
# ==========================
@login_required(login_url='/accounts/login/')
def dashboard(request):
    # جلب جميع الرسائل للمستخدم الحالي
    messages_list = Message.objects.filter(recipient=request.user).order_by('-send_at')
    return render(request, 'postbox/dashboard.html', {'messages': messages_list})

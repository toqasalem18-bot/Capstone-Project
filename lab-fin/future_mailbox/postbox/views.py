from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

# ==========================
#  قائمة الرسائل
# ==========================
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'postbox/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # عرض فقط الرسائل الخاصة بالمستخدم الحالي
        return Message.objects.filter(recipient=self.request.user).order_by('-send_at')

# ==========================
#  تفاصيل الرسالة
# ==========================
class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'postbox/message_detail.html'

# ==========================
#  إنشاء رسالة جديدة
# ==========================
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'postbox/message_form.html'
    success_url = reverse_lazy('postbox:dashboard')  # العودة للداش بورد بعد الحفظ

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        if obj.send_at and obj.send_at <= timezone.now():
            obj.is_sent = True  # تُرسل فوراً إذا الوقت الحالي أكبر أو يساوي
        obj.save()
        return super().form_valid(form)

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
            messages.error(request, "اسم المستخدم هذا موجود بالفعل 😅")
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

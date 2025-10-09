from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(pattern_name='postbox:timeline', permanent=False)),
    path('', include('postbox.urls')),  # تأكد أن urls الخاصة بالتطبيق مضمنة
]

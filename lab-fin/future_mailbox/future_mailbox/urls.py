from django.contrib import admin
from django.urls import path, include
from postbox.views import EventListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية توجه مباشرة للتايملاين
    path('', EventListView.as_view(), name='home'),

    # استدعاء جميع مسارات postbox
    path('', include('postbox.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

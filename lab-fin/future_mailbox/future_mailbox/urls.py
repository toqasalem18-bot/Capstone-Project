from django.contrib import admin
from django.urls import path, include
from postbox.views import EventListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية توجه مباشرة للتايملاين
    path('', EventListView.as_view(), name='home'),

    # استدعاء جميع مسارات postbox
    path('', include('postbox.urls')),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_admin_login(request):
    return redirect('/admin-login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', redirect_to_admin_login),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('Blogs.urls')),
    path('users/', include('Users.urls')),
    path('auth/', include('Authentication.urls')),
    path('profile/', include('Profiles.urls')),
    path('contacts/', include('ContactUs.urls')),
    path('projects/', include('Projects.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

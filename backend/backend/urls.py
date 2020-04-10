from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('backend.apps.api.urls', namespace='api')),
    path('uploads/', include('backend.apps.uploads.urls', namespace='uploads')),
    path('admin/', admin.site.urls)
]

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from backend.apps.uploads import views

app_name = 'uploads'
urlpatterns = [
    path('upload/', csrf_exempt(views.upload), name='upload'),
]

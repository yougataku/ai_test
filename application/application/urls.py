from django.urls import path
from .views import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
]

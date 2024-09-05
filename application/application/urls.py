from django.urls import path
from .views import views

urlpatterns = [
    path('about/', views.about, name='about'),
]

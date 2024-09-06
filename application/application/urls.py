from django.urls import path
from .views import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('registered-users/', views.registered_users_view, name='registered_users'),
]

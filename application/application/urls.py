from django.urls import path
from .views import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/<str:name>/<str:email>/', views.success, name='success'),
]

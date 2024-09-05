from django.urls import path
from .views import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
]

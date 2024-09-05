from django.contrib.auth import views as auth_views
from django.urls import path
from .views import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
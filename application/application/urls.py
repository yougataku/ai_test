from django.urls import path
from .views import views

urlpatterns = [
    path('success/<str:name>/<str:email>/', views.success, name='success'),
    path('contact/', views.contact_view, name='contact_url'),
]

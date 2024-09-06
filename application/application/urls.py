# urls.py
from django.urls import path
from .views import views

urlpatterns = [
    path('process-form/', views.process_form, name='process_form'),
    path('form/', views.form, name='form'),
]

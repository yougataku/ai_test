# urls.py
from django.urls import path
from .views.submit import submit
from .views.views import submit_form

urlpatterns = [
    path('submit/', submit, name='submit'),
    path('submit-form/', submit_form, name='submit_form'),
]
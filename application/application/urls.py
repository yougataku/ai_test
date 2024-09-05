from django.urls import path
from .views.view import contact_view, contact_list

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('contacts/', contact_list, name='contact_list'),
]
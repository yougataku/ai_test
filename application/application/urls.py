from django.urls import path
from application.views.view import contact_view, success


urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/<str:name>/<str:email>/', success, name='success'),

]

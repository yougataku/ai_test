from django.urls import path
from .views.views import sample_view, success

urlpatterns = [
    path('success/<str:name>/<str:email>/', success, name='success'),
    path('sample/', sample_view, name='sample'),
]
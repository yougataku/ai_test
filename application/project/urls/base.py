"""基本的なルーティング"""
from django.urls import include, path

urlpatterns = [
    path("api/", include("application.urls")),
]

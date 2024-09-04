from django.urls import include, path
from rest_framework.routers import DefaultRouter

from application.views.common.health_check import health_check

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("", include(router.urls)),
    path(r"health", health_check, name="health"),
]

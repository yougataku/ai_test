from django.urls import include, path
from rest_framework.routers import DefaultRouter

from application.views.common.health_check import health_check
from application.views.view import contact_view
from django.views.generic import TemplateView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("", include(router.urls)),
    path(r"health", health_check, name="health"),
    path('contact/', contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]

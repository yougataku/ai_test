from django.urls import path
from .views.views import home_view, contact_view, services_view
from application.views.common.health_check import health_check

urlpatterns = [
    path("", home_view, name="home"),
    path("contact/", contact_view, name="contact"),
    path("services/", services_view, name="services"),
    path("health", health_check, name="health"),
]

from django.contrib import admin
from django.urls import path

from .views import HealthCheck

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck', HealthCheck.as_view()),
]

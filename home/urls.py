from django.urls import path
from . import views
from .views import calendar_view

urlpatterns = [
    path("", views.home, name="home"),
    path('', calendar_view, name='calendar'), # Calendar
]
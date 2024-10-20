from django.urls import path
from django.urls import include, re_path
# from django.urls import url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
    # url(r’^calendar/$’, views.CalendarView.as_view(), name=’calendar’)
]
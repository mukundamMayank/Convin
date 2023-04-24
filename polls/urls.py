from django.urls import path

from . import views

urlpatterns = [
    path("rest/v1/calender/init/", views.GoogleCalendarInitView, name="index"),
    path("rest/v1/calender/redirect/", views.GoogleCalendarRedirectView, name="callist"),
]
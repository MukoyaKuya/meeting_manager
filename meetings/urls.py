# meetings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home dashboard
    path("", views.home, name="home"),

    # Meeting management
    path("create/", views.create_meeting, name="create_meeting"),
    path("meetings/", views.meeting_list, name="meeting_list"),
    path("meetings/<int:meeting_id>/", views.meeting_detail, name="meeting_detail"),
    path("meetings/<int:meeting_id>/edit/", views.edit_meeting, name="edit_meeting"),
    path("meetings/<int:meeting_id>/delete/", views.delete_meeting, name="delete_meeting"),
    path("all_meetings/", views.all_meetings, name="all_meetings"),
    path("signup/", views.signup_view, name="signup"),
]

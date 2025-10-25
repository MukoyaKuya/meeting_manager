# api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # ---------- JWT Authentication ----------
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ---------- Meeting Rooms ----------
    path("rooms/", views.MeetingRoomList.as_view(), name="room_list"),
    path("rooms/<int:pk>/", views.MeetingRoomDetail.as_view(), name="room_detail"),

    # ---------- Meetings ----------
    path("meetings/", views.MeetingList.as_view(), name="meeting_list"),
    path("meetings/<int:pk>/", views.MeetingDetail.as_view(), name="meeting_detail"),
]

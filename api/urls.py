from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingRoomViewSet, MeetingViewSet

router = DefaultRouter()
router.register(r'meetingrooms', MeetingRoomViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

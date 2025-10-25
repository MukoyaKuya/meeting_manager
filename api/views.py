from rest_framework import viewsets
from meetings.models import MeetingRoom, Meeting
from .serializers import MeetingRoomSerializer, MeetingSerializer

class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

# api/views.py
from rest_framework import generics, permissions
from meetings.models import Meeting, MeetingRoom
from .serializers import MeetingSerializer, MeetingRoomSerializer


# ---------- Meeting Rooms ----------
class MeetingRoomList(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeetingRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- Meetings ----------
class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]

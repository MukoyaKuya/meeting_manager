# api/serializers.py
from rest_framework import serializers
from meetings.models import Meeting, MeetingRoom


class MeetingRoomSerializer(serializers.ModelSerializer):
    """Serializer for MeetingRoom model"""
    class Meta:
        model = MeetingRoom
        fields = "__all__"


class MeetingSerializer(serializers.ModelSerializer):
    """Serializer for Meeting model with nested room info"""
    room = MeetingRoomSerializer(read_only=True)
    organizer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Meeting
        fields = "__all__"

from rest_framework import serializers
from meetings.models import MeetingRoom, Meeting

class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    room = MeetingRoomSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'

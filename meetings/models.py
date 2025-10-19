from django.db import models
from django.contrib.auth.models import User


class MeetingRoom(models.Model):
    """Represents a physical or virtual meeting room."""
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    """Stores meeting details, including uploaded minutes."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    minutes_file = models.FileField(upload_to="minutes/", blank=True, null=True)


    # New field for uploaded meeting minutes (PDF, DOCX, etc.)
    minutes_file = models.FileField(
        upload_to="meeting_minutes/",
        blank=True,
        null=True,
        help_text="Upload the official minutes document (PDF, DOCX, etc.)."
    )

    def __str__(self):
        return f"{self.title} ({self.room.name})"

    class Meta:
        ordering = ["-start_time"]
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

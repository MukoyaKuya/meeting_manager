# meetings/forms.py
from django import forms
from django.utils import timezone
from .models import Meeting
from zoneinfo import ZoneInfo

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["title", "description", "room", "start_time", "end_time"]

        widgets = {
            "start_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M"
            ),
            "end_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nairobi = ZoneInfo("Africa/Nairobi")

        # If instance has values, convert them to local Nairobi time
        for field in ["start_time", "end_time"]:
            value = self.initial.get(field)
            if value and timezone.is_aware(value):
                self.initial[field] = value.astimezone(nairobi).strftime("%Y-%m-%dT%H:%M")

    def clean(self):
        cleaned_data = super().clean()
        nairobi = ZoneInfo("Africa/Nairobi")

        # Convert naive local times to UTC for database storage
        for field in ["start_time", "end_time"]:
            dt = cleaned_data.get(field)
            if dt and dt.tzinfo is None:
                cleaned_data[field] = timezone.make_aware(dt, nairobi)
        return cleaned_data

from django import forms
from django.utils import timezone
from .models import Meeting
from zoneinfo import ZoneInfo


class MeetingForm(forms.ModelForm):
    """
    Form for creating and editing meetings, including optional minutes upload.
    Handles timezone conversion and preserves existing files on edit.
    """

    class Meta:
        model = Meeting
        fields = [
            "title",
            "description",
            "room",
            "start_time",
            "end_time",
            "minutes_file",  # Upload field for meeting minutes
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter meeting title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional meeting description",
                }
            ),
            "room": forms.Select(attrs={"class": "form-select"}),
            "start_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "minutes_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.doc,.docx,.txt",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nairobi = ZoneInfo("Africa/Nairobi")

        # Helps convert stored UTC times to Nairobi local for display
        for field in ["start_time", "end_time"]:
            value = self.initial.get(field)
            if value and timezone.is_aware(value):
                self.initial[field] = value.astimezone(nairobi).strftime("%Y-%m-%dT%H:%M")

        # Make file upload optional (even during edit)
        self.fields["minutes_file"].required = False

    def clean(self):
        cleaned_data = super().clean()
        nairobi = ZoneInfo("Africa/Nairobi")

        # Convert naive local times to UTC before saving
        for field in ["start_time", "end_time"]:
            dt = cleaned_data.get(field)
            if dt and dt.tzinfo is None:
                cleaned_data[field] = timezone.make_aware(dt, nairobi)

        # Validation: end_time must be after start_time
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("End time must be after the start time.")

        # Preserve existing minutes file if none uploaded during edit
        if not self.cleaned_data.get("minutes_file") and self.instance and self.instance.pk:
            cleaned_data["minutes_file"] = self.instance.minutes_file

        return cleaned_data

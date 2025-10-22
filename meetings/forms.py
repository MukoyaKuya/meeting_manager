from django import forms
from django.utils import timezone
from zoneinfo import ZoneInfo
from .models import Meeting
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MeetingForm(forms.ModelForm):
    """
    Form will help in creating and editing meetings, including optional minutes upload.
    It also handles timezone conversion and preserves existing files on edit.
    """
    class Meta:
        model = Meeting
        fields = [
            "title",
            "description",
            "room",
            "start_time",
            "end_time",
            "minutes_file",
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

        for field in ["start_time", "end_time"]:
            value = self.initial.get(field)
            if value and timezone.is_aware(value):
                self.initial[field] = value.astimezone(nairobi).strftime("%Y-%m-%dT%H:%M")

        self.fields["minutes_file"].required = False

    def clean(self):
        cleaned_data = super().clean()
        nairobi = ZoneInfo("Africa/Nairobi")

        for field in ["start_time", "end_time"]:
            dt = cleaned_data.get(field)
            if dt and dt.tzinfo is None:
                cleaned_data[field] = timezone.make_aware(dt, nairobi)

        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("End time must be after the start time.")

        if not self.cleaned_data.get("minutes_file") and self.instance and self.instance.pk:
            cleaned_data["minutes_file"] = self.instance.minutes_file

        return cleaned_data


# --------------------------------------------
# User Signup Form (Bootstrap + Conditional Help)
# --------------------------------------------
class CustomUserCreationForm(UserCreationForm):
    """
    The signup form styled with Bootstrap and conditional help text.
    It shows password rules only when validation fails.
    """
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label.lower()}",
            })

        # Helps hide help text initially (shown only after validation errors)
        for field in self.fields.values():
            field.help_text = ""

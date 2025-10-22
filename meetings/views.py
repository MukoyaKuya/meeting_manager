from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import MeetingForm, CustomUserCreationForm
from .models import Meeting


# -----------------------------------
# HOME DASHBOARD
# -----------------------------------
@login_required
def home(request):
    """User dashboard showing meeting stats for their own meetings only"""
    now = timezone.localtime()
    qs = Meeting.objects.filter(organizer=request.user)

    total_meetings = qs.count()
    upcoming_count = qs.filter(start_time__gt=now).count()
    ongoing_count = qs.filter(start_time__lte=now, end_time__gte=now).count()
    ended_count = qs.filter(end_time__lt=now).count()

    context = {
        "total_meetings": total_meetings,
        "upcoming_count": upcoming_count,
        "ongoing_count": ongoing_count,
        "ended_count": ended_count,
        "now": now,
    }
    return render(request, "meetings/home.html", context)


# -----------------------------------
# CREATE MEETING (with conflict check)
# -----------------------------------
@login_required
def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST, request.FILES)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.organizer = request.user

            # Prevent booking conflict (same room overlapping time)
            conflict_exists = Meeting.objects.filter(
                room=meeting.room,
                start_time__lt=meeting.end_time,
                end_time__gt=meeting.start_time,
            ).exists()

            if conflict_exists:
                messages.error(
                    request,
                    f"A meeting already exists in {meeting.room.name} during this time. Please choose another slot.",
                )
                return render(request, "meetings/create_meeting.html", {"form": form})

            meeting.save()
            messages.success(request, "Meeting created successfully!")
            return redirect("meeting_list")

        messages.error(request, "Please correct the errors below.")
    else:
        form = MeetingForm()
    return render(request, "meetings/create_meeting.html", {"form": form})


# -----------------------------------
# USER’S MEETINGS LIST (PRIVATE)
# -----------------------------------
@login_required
def meeting_list(request):
    """Shows ONLY meetings created by the logged-in user"""
    now = timezone.localtime()
    qs = Meeting.objects.filter(organizer=request.user).order_by("-start_time")

    # Filters
    q = (request.GET.get("q") or "").strip()
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(room__name__icontains=q)
        )

    status = (request.GET.get("status") or "all").lower()
    if status == "upcoming":
        qs = qs.filter(start_time__gt=now)
    elif status == "ongoing":
        qs = qs.filter(start_time__lte=now, end_time__gte=now)
    elif status == "ended":
        qs = qs.filter(end_time__lt=now)

    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    if date_from:
        qs = qs.filter(start_time__date__gte=date_from)
    if date_to:
        qs = qs.filter(start_time__date__lte=date_to)

    try:
        per_page = int(request.GET.get("per_page", 10))
    except ValueError:
        per_page = 10

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "meetings": page_obj.object_list,
        "page_obj": page_obj,
        "paginator": paginator,
        "now": now,
        "q": q,
        "status": status,
        "date_from": date_from or "",
        "date_to": date_to or "",
        "per_page": per_page,
    }
    return render(request, "meetings/meeting_list.html", context)


# -----------------------------------
# ALL MEETINGS (READ-ONLY)
# -----------------------------------
@login_required
def all_meetings(request):
    """
    Displays ALL meetings from all users (read-only view).
    """
    now = timezone.localtime()
    qs = Meeting.objects.all().order_by("-start_time")

    q = (request.GET.get("q") or "").strip()
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(room__name__icontains=q)
            | Q(organizer__username__icontains=q)
        )

    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "meetings": page_obj.object_list,
        "page_obj": page_obj,
        "paginator": paginator,
        "now": now,
        "q": q,
    }
    return render(request, "meetings/all_meetings.html", context)


# -----------------------------------
# MEETING DETAILS
# -----------------------------------
@login_required
def meeting_detail(request, meeting_id):
    """Show meeting details (any user can view)"""
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


# -----------------------------------
# EDIT MEETING (with file upload)
# -----------------------------------
@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)

    if request.method == "POST":
        form = MeetingForm(request.POST, request.FILES, instance=meeting)
        if form.is_valid():
            updated = form.save(commit=False)

            overlap = Meeting.objects.filter(
                room=updated.room,
                start_time__lt=updated.end_time,
                end_time__gt=updated.start_time,
            ).exclude(id=meeting.id).exists()

            if overlap:
                messages.error(
                    request,
                    f"Another meeting already exists in {updated.room.name} at that time.",
                )
                return render(
                    request,
                    "meetings/meeting_edit.html",
                    {"form": form, "meeting": meeting},
                )

            updated.save()
            messages.success(request, "Meeting updated successfully (including minutes if uploaded).")
            return redirect("meeting_detail", meeting_id=meeting.id)
        messages.error(request, "Please correct the errors below.")
    else:
        form = MeetingForm(instance=meeting)

    return render(
        request, "meetings/meeting_edit.html", {"form": form, "meeting": meeting}
    )


# -----------------------------------
# DELETE MEETING
# -----------------------------------
@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)
    if request.method == "POST":
        meeting.delete()
        messages.warning(request, "Meeting deleted.")
        return redirect("meeting_list")
    return render(
        request, "meetings/meeting_confirm_delete.html", {"meeting": meeting}
    )


# -----------------------------------
# MINUTES REPOSITORY (NEW)
# -----------------------------------
@login_required
def minutes_repository(request):
    """Displays all meetings that have uploaded minutes"""
    now = timezone.localtime()
    qs = Meeting.objects.filter(minutes_file__isnull=False).exclude(minutes_file="").order_by("-start_time")

    q = (request.GET.get("q") or "").strip()
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(room__name__icontains=q)
            | Q(organizer__username__icontains=q)
        )

    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "meetings": page_obj.object_list,
        "page_obj": page_obj,
        "paginator": paginator,
        "now": now,
        "q": q,
    }
    return render(request, "meetings/minutes_repository.html", context)


# -----------------------------------
# USER SIGNUP (Fixed version)
# -----------------------------------
def signup_view(request):
    """
    Handles new user registration using CustomUserCreationForm.
    Hides password rules until errors appear.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully. Welcome!")
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()

    # Hide verbose help text until there's an error
    if not form.errors:
        for field_name in form.fields:
            form.fields[field_name].help_text = None

    return render(request, "registration/signup.html", {"form": form})

# meetings/views.py
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from zoneinfo import ZoneInfo  

from .forms import MeetingForm
from .models import Meeting

# Define the Nairobi timezone
NAIROBI_TZ = ZoneInfo("Africa/Nairobi")


# 🏠 Home Page — Dashboard summary
@login_required
def home(request):
    now = timezone.now().astimezone(NAIROBI_TZ)
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


# ➕ Create Meeting
@login_required
def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.organizer = request.user
            meeting.save()
            messages.success(request, "✅ Meeting created successfully!")
            return redirect("meeting_list")
        messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = MeetingForm()
    return render(request, "meetings/create_meeting.html", {"form": form})


# 📋 Meeting List with Search + Filter + Pagination
@login_required
def meeting_list(request):
    """
    Supports filters:
      - q: search by title, description, or room
      - status: upcoming|ongoing|ended|all
      - date_from / date_to
      - per_page (default 10)
    """
    now = timezone.now().astimezone(NAIROBI_TZ)
    qs = Meeting.objects.filter(organizer=request.user).order_by("-start_time")

    # 🔍 Search
    q = (request.GET.get("q") or "").strip()
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(description__icontains=q)
            | Q(room__name__icontains=q)
        )

    # ⚙️ Status Filter
    status = (request.GET.get("status") or "all").lower()
    if status == "upcoming":
        qs = qs.filter(start_time__gt=now)
    elif status == "ongoing":
        qs = qs.filter(start_time__lte=now, end_time__gte=now)
    elif status == "ended":
        qs = qs.filter(end_time__lt=now)

    # 📆 Date Range Filters
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    if date_from:
        qs = qs.filter(start_time__date__gte=date_from)
    if date_to:
        qs = qs.filter(start_time__date__lte=date_to)

    # 📑 Pagination
    try:
        per_page = int(request.GET.get("per_page", 10))
        if per_page <= 0:
            per_page = 10
    except ValueError:
        per_page = 10

    paginator = Paginator(qs, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

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


# 📄 Meeting Details
@login_required
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


# Edit Meeting
@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            messages.success(request, "Meeting updated successfully.")
            return redirect("meeting_detail", meeting_id=meeting.id)
        messages.error(request, "Please correct the errors below.")
    else:
        form = MeetingForm(instance=meeting)

    return render(
        request, "meetings/meeting_edit.html", {"form": form, "meeting": meeting}
    )


# 🗑️ Delete Meeting
@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)
    if request.method == "POST":
        meeting.delete()
        messages.warning(request, "Meeting deleted successfully.")
        return redirect("meeting_list")
    return render(
        request, "meetings/meeting_confirm_delete.html", {"meeting": meeting}
    )


# Signup
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "🎉 Account created successfully. Welcome!")
            return redirect("home")
        messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

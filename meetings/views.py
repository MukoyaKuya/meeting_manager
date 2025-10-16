from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import MeetingForm
from .models import Meeting


# 🏠 Home Page
@login_required
def home(request):
    return render(request, 'meetings/home.html')


# helps create Meeting
@login_required
def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.organizer = request.user
            meeting.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/create_meeting.html', {'form': form})


# List Meetings
@login_required
def meeting_list(request):
    meetings = Meeting.objects.filter(organizer=request.user).order_by('-start_time')
    return render(request, 'meetings/meeting_list.html', {'meetings': meetings})


# Meeting Details
@login_required
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})


#Edit Meeting
@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting_detail', meeting_id=meeting.id)
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'meetings/meeting_edit.html', {'form': form, 'meeting': meeting})


#Delete Meeting
@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id, organizer=request.user)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_list')
    return render(request, 'meetings/meeting_confirm_delete.html', {'meeting': meeting})


# 🧍‍♂️ Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.organizer = request.user
            meeting.save()
            messages.success(request, "Meeting created successfully!")
            return redirect("meeting_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MeetingForm()
    return render(request, "meetings/create_meeting.html", {"form": form})


@login_required
def delete_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk, organizer=request.user)
    meeting.delete()
    messages.warning(request, "Meeting deleted successfully.")
    return redirect("meeting_list")
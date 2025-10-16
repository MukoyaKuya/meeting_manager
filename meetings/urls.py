from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_meeting, name='create_meeting'),
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('meetings/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
    path('meetings/<int:meeting_id>/edit/', views.edit_meeting, name='edit_meeting'),  #  added edit feature
    path('meetings/<int:meeting_id>/delete/', views.delete_meeting, name='delete_meeting'),  # added delete feature
]

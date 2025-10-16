from django.contrib import admin
from .models import MeetingRoom, Meeting

@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'created_at')
    search_fields = ('name', 'location')

    # Only superusers or staff can add/delete rooms
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'room', 'start_time', 'end_time', 'is_active')
    list_filter = ('room', 'is_active', 'start_time')
    search_fields = ('title', 'description', 'organizer__username')

    # Anyone (staff or normal user) can add a meeting, but only admin can delete
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def save_model(self, request, obj, form, change):
        if not change or not obj.organizer:
            obj.organizer = request.user
        obj.save()


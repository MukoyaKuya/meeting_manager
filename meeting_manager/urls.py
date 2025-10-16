from django.contrib import admin
from django.urls import path, include
from meetings import views as meeting_views
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meetings.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # includes login/logout views by default
    path('signup/', meeting_views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

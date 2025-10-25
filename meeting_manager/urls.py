# meeting_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ---------- ADMIN ----------
    path("admin/", admin.site.urls),

    # ---------- AUTHENTICATION ----------
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),

    # ---------- MAIN APP ROUTES ----------
    path("", include("meetings.urls")),          # main web app (HTML templates)

    # ---------- API ROUTES ----------
    path("api/", include("api.urls")),           # all REST endpoints (JWT + CRUD)
    path("api-auth/", include("rest_framework.urls")),  # optional browser login for DRF
]

# ---------- DEVELOPMENT: MEDIA & STATIC ----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

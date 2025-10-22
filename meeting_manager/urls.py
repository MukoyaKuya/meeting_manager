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

    # ---------- APP ROUTES ----------
    path("", include("meetings.urls")),
]

# ---------- DEVELOPMENT: MEDIA & STATIC ----------
if settings.DEBUG:
    # Serve uploaded files (meeting minutes, images) during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Optional: serve static files too if not using collectstatic locally
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

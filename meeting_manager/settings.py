from pathlib import Path
import os  # Required for environment variables

# ---------- BASE DIRECTORY ----------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------- SECURITY ----------
# SECRET_KEY — Read from environment on Render, fallback for local dev
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-!23&a7-41r(os8!#@@r1&)wqjl^$gdgcuw!4+g%y!%l5ocfnd2"
)

# DEBUG — False in production (Render), True locally
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS — Include Render domain as fallback to prevent DisallowedHost
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "mkutano-io.onrender.com,.onrender.com,127.0.0.1,localhost"
).split(",")


# ---------- INSTALLED APPS ----------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "meetings",
    "api",
]


# ---------- MIDDLEWARE ----------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------- URL & WSGI ----------
ROOT_URLCONF = "meeting_manager.urls"
WSGI_APPLICATION = "meeting_manager.wsgi.application"


# ---------- TEMPLATES ----------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.tz",
            ],
        },
    },
]


# ---------- DATABASE ----------
# (SQLite for now — can switch to PostgreSQL on Render later)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------- PASSWORD VALIDATORS ----------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------- TIMEZONE & LOCALIZATION ----------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_TZ = True
USE_L10N = False

DATETIME_FORMAT = "M d, Y h:i A"
TIME_FORMAT = "h:i A"


# ---------- STATIC FILES ----------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


# ---------- MEDIA FILES ----------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ---------- AUTHENTICATION ----------
LOGIN_REDIRECT_URL = "home"
LOGIN_URL = "/accounts/login/"
LOGOUT_REDIRECT_URL = "login"


# ---------- DEFAULT PRIMARY KEY FIELD ----------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ---------- DJANGO REST FRAMEWORK ----------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}


# ---------- PRODUCTION SECURITY RECOMMENDATIONS ----------
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

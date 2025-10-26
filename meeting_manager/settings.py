from pathlib import Path

# ---------- BASE DIRECTORY ----------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------- SECURITY ----------
SECRET_KEY = "django-insecure-!23&a7-41r(os8!#@@r1&)wqjl^$gdgcuw!4+g%y!%l5ocfnd2"
DEBUG = True
ALLOWED_HOSTS: list[str] = []  # Add domain/IP here when deploying

# ---------- INSTALLED APPS ----------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "meetings",  
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
        "DIRS": [],  # Django will use app templates automatically
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
# URL to access static files
STATIC_URL = "/static/"

# Folders Django searches for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "static",  # global static folder 
]

# Folder where Django collects all static files during deployment
STATIC_ROOT = BASE_DIR / "staticfiles"

# ---------- MEDIA FILES ----------
# Media files are user-uploaded content (e.g., meeting minutes)
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


from datetime import timedelta
from pathlib import Path
import os

# ------------------------------
# Base Paths
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Security
# ------------------------------
SECRET_KEY = 'your-secret-key-here'  # CHANGE in production!
DEBUG = False  # False in production
ALLOWED_HOSTS = ['*']  # Replace with your domain in production

# ------------------------------
# Installed Apps
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',         # Admin site
    'django.contrib.auth',          # Auth system
    'django.contrib.contenttypes',  # Needed for auth and admin
    'django.contrib.sessions',      # Session support
    'django.contrib.messages',      # Messages framework
    'django.contrib.staticfiles',   # Required for admin static files


    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',   # For Flutter web / cross-origin requests

    'crud',
    'user',
]

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',       # Keep at top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # <-- add this
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',   # <-- add this
]











TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add paths to your custom templates if any
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ------------------------------
# URL & WSGI
# ------------------------------
ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# ------------------------------
# Database
# ------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use PostgreSQL for production
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------
# Password Validation
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# Internationalization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static & Media Files
# ------------------------------
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ------------------------------
# DRF + JWT Configuration
# ------------------------------
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'myproject.core.renderers.CustomJSONRenderer',  # global response wrapper
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # default permission
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ------------------------------
# CORS for Flutter App
# ------------------------------
CORS_ALLOW_ALL_ORIGINS = True  # Dev only! Restrict to your Flutter app URL in production

# ------------------------------
# Default Primary Key
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

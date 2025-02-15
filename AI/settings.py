"""
Django settings for AI project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t_mvnefq4m*l_z&u0klp@_7tzh%i_ybw_j-+x1-@&_5k(^c+ow'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'corsheaders',
    
    'django_chapa',
    'core',
    'claims',
    'policies',
    'payment',
    'accounts',
    'vehicle',
    'risk',
]

CHAPA_SECRET = "Secret"
CHAPA_API_URL = ''
CHAPA_API_VERSION = 'v1'
CHAPA_TRANSANCTION_MODEL = 'AI-INSURANCE.chapa_model'


# Authentication and Permissions
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'AUTH_HEADER_TYPES': ('Bearer',),  # Ensuring it matches frontend usage
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

AUTH_USER_MODEL = 'core.User'


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Cross-Origin Resource Sharing (CORS) Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_HTTPONLY = False


# URLs and Templates
ROOT_URLCONF = 'AI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AI.wsgi.application'


# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'PORT': '5432'
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Djoser Customization
DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USER_SERIALIZER': 'core.serializers.CustomUserCreateSerializer',
}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static Files
STATIC_URL = 'static/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

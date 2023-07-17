"""
Django settings for my_game_list project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dotenv
import dj_database_url
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#zn%(je9uj%dv36nyc#6^t&a8zrb)p-m&-eo%fs23=^zear#f5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_spectacular",
   
]

MY_APPS = [
    "games",
    "genders",
    "reviews",
    "users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "my_game_list.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "my_game_list.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

dotenv.load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')



DATABASES = {
   
      "default": {
     
      "ENGINE": "django.db.backends.postgresql",
      "NAME": os.getenv("POSTGRES_DB"),
      "USER": os.getenv("POSTGRES_USER"),
      "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
      "HOST": "127.0.0.1",
      "PORT": 5432,
  
    }
}

DATABASE_URL= os.getenv("DATABASE_URL")
db_deploy = dj_database_url.config(default=DATABASE_URL)
if DATABASE_URL:
    DATABASES["default"].update(db_deploy)
    DEBUG = False


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SIMPLE_JWT ={
    "ACCESS_TOKEN_LIFETIME" : timedelta(minutes=24),
    "REFRESH_TOKEN" : timedelta(minutes=24)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
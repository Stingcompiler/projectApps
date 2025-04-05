"""
Django settings for projectApps project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e2!07$nkot=mai!4=&*-n7s-0eragf13^bja&xy+(&%36tw#eg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
"""

"""
ALLOWED_HOSTS = ['musab.stingdev.uk','http://127.0.0.1:8000/admin/']
CSRF_TRUSTED_ORIGINS = [
    "https://musab.stingdev.uk",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... other core middleware
    'news.middleware.VisitorTrackingMiddleware',
    # ... your other custom middleware
    # ... other core middleware
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'comments',
    'news',
    'users',
    'adminPannel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectApps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'projectApps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'journal',  # اسم قاعدة البيانات
        'USER': 'postgres',      # اسم المستخدم
        'PASSWORD': 'sting',  # كلمة المرور
        'HOST': 'localhost',  # أو عنوان السيرفر إذا كان بعيدًا
        'PORT': '5432',  # البورت الافتراضي
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = '/static/' 

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Using pathlib for better path handling
]

STATIC_ROOT = BASE_DIR / "staticfiles"  
# This is needed for `collectstatic`

MEDIA_URL = '/media/'  
MEDIA_ROOT = BASE_DIR / "media"  
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #Or another backend.
EMAIL_HOST = 'smtp.gmail.com' # Or your email provider's SMTP server
EMAIL_PORT = 587  # Or the appropriate port
EMAIL_USE_TLS = True # Or EMAIL_USE_SSL
EMAIL_HOST_USER = 'musabsting277@gmail.com' # Your email address
EMAIL_HOST_PASSWORD = 'Profsting12@@@@' # Your email password or app password
RECIPIENT_ADDRESS = 'musabsting277@gmail.com' #The email address that receives the contact form data.

"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 587 for TLS, or 465 for SSL
EMAIL_USE_TLS = True  # Set to False if using SSL
EMAIL_USE_SSL = False  # If using SSL, set this to True and TLS to False
EMAIL_HOST_USER = 'musabsting277@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'atyg hdnc waue plyb'
RECIPIENT_ADDRESS = 'musabsting277@gmail.com'

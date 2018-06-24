"""
Django settings for billeterie project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h%!eq=h1$zk=s1a4hrul8@(-ub)xws4ta7m85e^tfld!f6w-#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]

# Application definition

INSTALLED_APPS = [
    'social_django',
    'epita_connect',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'paypal.standard.ipn',
    'database',
    'util',
    'api'
    ]

PAYPAL_TEST = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'billeterie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'epita_connect.backend.EpitaOpenIdConnect',  # for OpenId cri Epita authentification
    'django.contrib.auth.backends.ModelBackend',
    )

WSGI_APPLICATION = 'billeterie.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '207735899591-d34tqq7bvnk521ks4lrv825pfqopnos6.apps.googleusercontent.com'  # Paste
# CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WWY5kMbRv9Y1UWuGoTd8eeSw'  # Paste Secret Key

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_EPITA_KEY = '031021'
SOCIAL_AUTH_EPITA_SECRET = '97593354782061112fdeab765fd8faf9694903adfd8fa2d345a46be1'
SOCIAL_AUTH_EPITA_SCOPE = ['epita']
SOCIAL_AUTH_EPITA_EXTRA_DATA = ['promo']
SOCIAL_AUTH_EPITA_BETA = False

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_USE_TLS = True

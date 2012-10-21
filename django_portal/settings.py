#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django settings for django_asistencia project.

import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Leonardo Gatica', 'lgaticastyle@gmail.com'), )

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'elearning.UserProfile'
LOGIN_REDIRECT_URL = '/'

# ENGINES: 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
# NAME: name database or path to database file if using sqlite3.
# USER: Not used with sqlite3.
# PASSWORD: Not used with sqlite3.
# HOST: Default localhost. Not used with sqlite3. Set /tmp if use postgresql
# PORT: Set to empty string for default. Not used with sqlite3.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'escaleno.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Santiago'

LANGUAGE_CODE = 'es-cl'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = False

MEDIA_ROOT = os.path.join(RUTA_PROYECTO, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(RUTA_PROYECTO, 'static'), )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

SECRET_KEY = 'tuj_bop#$7x8*2j@!x26gqn9nwf_#(c#gf*y=ea+m442q-ht6('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'django_portal.urls'

WSGI_APPLICATION = 'django_portal.wsgi.application'

TEMPLATE_DIRS = (os.path.join(RUTA_PROYECTO, 'templates'), )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'elearning',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR', 'propagate': True
        }
    },
}

LOGIN_URL = '/login'

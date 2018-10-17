"""
Django settings for fgtautoscale project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c5sn$)(z@ww6(xo8bwm3vaq(z4t)io&!e9&_px^546m2f^iah)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fgtautoscale',
]

#    'django_zappa.middleware.ZappaMiddleware',
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fgtautoscale.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'fgtautoscale.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'fgtautoscale.const': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },'fgtautoscale.views': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'fgtautoscale.scheduled': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'fgtautoscale.AutoScaleGroup': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'fgtautoscale.Fortigate': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'fortiguru',
        'USER': 'fortiguru',
        'PASSWORD': 'fortiguru',
        'HOST': 'fortiguru2.cunvktpp9sqc.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

ZAPPA_SETTINGS = {
    'dev': {
        's3_bucket': 'mdw-lambda',
        'settings_file': './fgtautoscale/dev_lambda_settings.py',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

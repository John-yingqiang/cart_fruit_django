# -*- coding: utf-8 -*-
"""
Django settings for Thai project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT=os.path.join(os.path.abspath(os.path.dirname(__file__)),'..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q#+5q3hhm5#c+ogm=!v=@!s)5kl!^7k)f+dnk9g3nvph#hbr_6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'www.thaifruit1975.com']


# Application definition

INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'fruit.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'compressor',
    'debug_toolbar',
    'fruit',
    'taggit',
    'gunicorn',
    'cart',
    'orders',
    'upload',
    'rest_framework',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
CONFIG_DEFAULTS = {
        'JQUERY_URL':'//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
        }

INTERNAL_IPS = ('118.31.43.180',)
ROOT_URLCONF = 'Thai.urls'

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

WSGI_APPLICATION = 'Thai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql', # 提示连接mysql数据库  
        'NAME': 'fruit', # 数据库名为test，要自己创建  
        'USER': 'root', # 用户名  
        'PASSWORD': 'root', # 密码  
        'HOST': '127.0.0.1', # 连接的主机  
        'PORT': '3306', # 对应的端口号  
    }  
} 

CACHE_BACKEND = 'memcached://127.0.0.1:11211'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
        'EXCEPTION_HANDLER':(
            'common.return_format.custom_exception_handler'
            )
        }

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'zh-Hans'
# TIME_ZONE = 'UTC'
TIME_ZONE='Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'fruit')
MEDIA_URL = '/fruit/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
from django.conf import global_settings
FILE_UPLOAD_HANDLERS = ['upload.upload_progress.UploadProgressCachedHandler',] + global_settings.FILE_UPLOAD_HANDLERS

CART_SESSION_ID = 'cart'

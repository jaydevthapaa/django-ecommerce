"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jlrq33r&xw9vse6=f_iylhh&p$7vtlc+y(oi&0s1+u$)q$mxlj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store',
    #
    # 'user_authentication',
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'ecommerce/store/registration'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'



STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Optionally (used only if you run collectstatic):
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

MEDIA_URL='/images/'
MEDIA_ROOT= os.path.join(BASE_DIR,'static/css/images')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# eSewa Payment Gateway Settings

ESEWA_MERCHANT_ID = 'EPAYTEST'
ESEWA_SECRET_KEY = '8gBm/:&EnhH.1/q'
ESEWA_URL = 'https://rc-epay.esewa.com.np/api/epay/main/v2/form'
ESEWA_VERIFY_URL = 'https://rc-epay.esewa.com.np/api/epay/v2/verification/'
ESEWA_VERIFY_URL_V1 = 'https://rc-epay.esewa.com.np/api/epay/transrec'
ESEWA_ENV = 'RC'  # or 'PROD'
ESEWA_SUCCESS_URL = 'http://127.0.0.1:8000/payment/success/'
ESEWA_FAILURE_URL = 'http://127.0.0.1:8000/payment/failure/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
        'file': {'class': 'logging.FileHandler', 'filename': 'payment_debug.log'},
    },
    'loggers': {
        'store.views': {'handlers': ['console','file'], 'level': 'DEBUG'},
        'store.esewa_utils': {'handlers': ['console','file'], 'level': 'DEBUG'},
    },
}

# eSewa Payment Configuration
# Add these to your settings.py file

# Set to True for testing, False for production
ESEWA_TEST_MODE = True  # Change to False for production

# eSewa Merchant Credentials
if ESEWA_TEST_MODE:
    # Test credentials
    ESEWA_MERCHANT_ID = 'EPAYTEST'
    ESEWA_SECRET_KEY = '8gBm/:&EnhH.1/q'
else:
    # Production credentials (get these from your eSewa merchant account)
    ESEWA_MERCHANT_ID = 'YOUR_PRODUCTION_MERCHANT_ID'
    ESEWA_SECRET_KEY = 'YOUR_PRODUCTION_SECRET_KEY'

# Optional: Add these URLs to your settings for reference
ESEWA_URLS = {
    'test': {
        'payment': 'https://rc-epay.esewa.com.np/api/epay/main/v2/form',
        'verification': 'https://rc-epay.esewa.com.np/api/epay/transaction/status/'
    },
    'production': {
        'payment': 'https://epay.esewa.com.np/api/epay/main/v2/form',
        'verification': 'https://epay.esewa.com.np/api/epay/transaction/status/'
    }
}
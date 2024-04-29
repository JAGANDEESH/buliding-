"""
Django settings for building_construction project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qy99_@e#dcu^cbt$=dazit$_*)5yz*)f_6cmkpxu9r-a9)iq90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'c893-103-175-108-62.ngrok-free.app']

ACCESS_CONTROL_ALLOW_HEADERS = True
ACCESS_CONTROL_ALLOW_HEADERS = [
    'https://c893-103-175-108-62.ngrok-free.app',
    'http://localhost:3000',
    # 'https://sandbox.cashfree.com/pg/sdk/js/ping',
    'https://sdk.cashfree.com',
    'ngrok-skip-browser-warning',
    'https://api.in.kaleyra.io/v1/HXIN1756628118IN/verify',
]
# CORS_URLS_REGEX = '^/v1/HXIN1756628118IN/verify/$'

CORS_ALLOWED_ORIGIN_REGEXES = [
    'https://api.in.kaleyra.io/v1/HXIN1756628118IN/verify',
    'https://api\.in\.kaleyra\.io',
    # Add other allowed origins using regex if needed
]
CORS_ALLOWED_ORIGINS = [
    'https://api.in.kaleyra.io',
    'http://localhost:19006',
    'http://127.0.0.1:19006',
    'https://7c8b-106-51-82-33.ngrok-free.app',
    'http://localhost:3000',
    'http://127.0.0.1',
    'http://127.0.0.1:8080',
    'http://43.254.41.63:8080',
    'http://superapp.kalyanicrm.com',
    'https://7c8b-106-51-82-33.ngrok-free.app',
    'http://localhost:3000',
    # 'https://sandbox.cashfree.com/pg/sdk/js/ping',
    'https://sdk.cashfree.com',
    # 'https://api.in.kaleyra.io/v1/HXIN1756628118IN/verify',
    
]
LOGIN_REDIRECT_URL = '/dashboard/'  # Redirect users after login


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'profile_utility'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'building_construction.urls'

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

WSGI_APPLICATION = 'building_construction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buildconst',
        'HOST':'buildconst.cluster-c78m8cwuy9ux.us-east-1.rds.amazonaws.com',
        'PORT':'3306',
        'USER':'admin',
        'PASSWORD':'jaganvasagar',
    }
} 

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

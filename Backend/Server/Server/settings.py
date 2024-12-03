"""
Django settings for Server project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-alm5e6@tia&ocbeq8*9ed4zvlqs1a^=x#*nydf#6el!tn5o9rv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Third Party Admin Liberaries
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third Party Liberaries
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    
    # Costume apps
    'Blogs.apps.BlogsConfig',
    'Users.apps.UsersConfig',
    'Profiles.apps.ProfilesConfig',
    'Authentication.apps.AuthenticationConfig',
    'ContactUs.apps.ContactusConfig',
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

ROOT_URLCONF = 'Server.urls'

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

WSGI_APPLICATION = 'Server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "Codingo AdminPanel",
    "site_header": "Codingo Plus Administration",
    "site_brand": "Codingo Plus",
    "welcome_sign": "Welcome to My Codingo Plus Admin",
    "copyright": "Codingo Plus",
    "search_model": "auth.User",  # Set your search model
    "user_avatar": "path/to/your/avatar.png",  # Path to user avatar image

    # Top menu settings
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Documentation", "url": "https://docs.djangoproject.com/en/stable/", "new_window": True},
        {"model": "auth.User"},
        {"model": "auth.Group"},
    ],

    # Customizing the sidebar
    "user_menu": "django.contrib.auth.models.User",
    "show_sidebar": True,
    "sidebar": True,
    "sidebar_menu": [
        {"name": "Dashboard", "url": "admin:index"},
        {"name": "Blogs", "url": "admin:Blogs_blog_changelist"},
        {"name": "Users", "url": "admin:auth_user_changelist"},
    ],
   # Path to your custom JS

    # Theme settings
    "theme": "dark",  # Choose from 'default', 'dark', 'light', or custom themes
    "color_scheme": "default",  # You can set a color scheme here

    # Other settings
    "show_ui_builder": True,  # Show the UI builder button
    "show_settings": True,     # Show the settings button
    "show_logout": True,       # Show the logout button
}

# Auth user model
AUTH_USER_MODEL = 'Users.User'

# Rest framework
REST_FRAMEWORK = {
    #  Authentications classes
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# JWT settings
SIMPLE_JWT = {
    #  Tokens life time
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    
    #  Refresh tokens
    'ROTATE_REFRESH_TOKENS': True,
    
    # Blacklist 
    'BLACKLIST_AFTER_ROTATION': True,
    
    # Last Login refreshing
    'UPDATE_LAST_LOGIN': True,
    
    # Algorithm
    'ALGORITHM': 'HS256',
    
    # Verifying key 
    'VERIFYING_KEY': None,
    
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    
    # Headers 
    'AUTH_HEADER_TYPES': ('Bearer',),     # Header type
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',   # Header name
    
    # User id setting
    'USER_ID_FIELD': 'id',         # Field
    'USER_ID_CLAIM': 'user_id',    # Claim
    
    #  Auth rules settings
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    
    # Auth token classes and settings
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
    'JTI_CLAIM': 'jti',
    
    #  Sliding settings
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # Token sliding lifetime
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_ALL_ORIGINS = True


# Emailing Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'venus.pws-dns.net'
EMAIL_HOST_USER = 'email@hip-hop-tweety.com'
EMAIL_HOST_PASSWORD = 't4xxohmp5o6t'
EMAIL_PORT = 587
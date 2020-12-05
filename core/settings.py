"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = [
    'ssm-product-api.pipe.my',
    '127.0.0.1',
    '10.200.22.127',
    'localhost',
    'afeezaziz.ngrok.io',
    'syafiqbasri.ngrok.io',
    'identitypro.ssm.com.my',
    '*'
]

USE_X_FORWARDED_PORT = True

# Application definition

INSTALLED_APPS = [
    # 'core.middleware.MultipleProxyMiddleware',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'django.contrib.humanize',
    'django_saml2_auth',

    'anymail',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  #
    'corsheaders',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'simple_history',
    'sslserver',

    'carts',
    'entities',
    'freeforms',
    'organisations',
    'products',
    'quotas',
    'services',
    'transactions',
    'tickets',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # for reporting template
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',#'django_multitenant.backends.postgresql',#'django.contrib.gis.db.backends.postgis',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'DISABLE_SERVER_SIDE_CURSORS': True
    }
}

# INFORMIX

# 'default': {
#     'ENGINE': 'django_informixdb',
#     'NAME': 'myproject',
#     'SERVER': 'ifxserver',
#     'USER' : 'sysadmin',
#     'PASSWORD': 'P@ssw0rd',
#     'OPTIONS': {
#         'DRIVER': '/path/to/iclit09b.so'. # Or iclit09b.dylib on macOS
#         'CPTIMEOUT': 120,
#         'CONN_TIMEOUT': 120,
#         'ISOLATION_LEVEL': 'READ_UNCOMMITTED',
#         'LOCK_MODE_WAIT': 0,
#         'VALIDATE_CONNECTION': True,
#     },
#     'CONNECTION_RETRY': {
#         'MAX_ATTEMPTS': 10,
#     },
#     'TEST': {
#         'NAME': 'portal',
#         'CREATE_DB': False
#     }
# }


import dj_database_url
db_from_env = dj_database_url.config(default=config('DATABASE_URL'), conn_max_age=500)
DATABASES['default'].update(db_from_env)

if any(db_from_env):
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'https://ssm-product-api.pipe.my',
    'http://127.0.0.1',
    'http://localhost',
    'https://identitypro.ssm.com.my',
    'http://10.200.22.127:8000'
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'https://ssm-product-api.pipe.my',
    'http://127.0.0.1',
    'http://localhost',
    'https://identitypro.ssm.com.my',
    'http://10.200.22.127:8000'
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
AWS_DEFAULT_ACL = 'public-read'

SITE_ID = 1

REST_USE_JWT = True

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': config('SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SSO SAML
SAML_FOLDER = os.path.join(BASE_DIR, 'saml')
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SSO SAML

AUTH_USER_MODEL = 'users.CustomUser'

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    'METADATA_AUTO_CONF_URL': 'https://identitypro.ssm.com.my:8443/nidp/saml2/metadata',
    # 'METADATA_LOCAL_FILE_PATH': 'acs/sp-metadata.xml',

    # Optional settings below
    # 'DEFAULT_NEXT_URL': '/auth/login',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': False,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'ssmEServicesName',
        'username': 'ssmADUserID',
        'full_name': 'fullName',
        'identification_type': 'ssmIDType',
        'nric_number': 'ssmNRIC',
        'address_1': 'ssmHomeAdd01',
        'address_2': 'ssmHomeAdd02',
        'address_3': 'ssmHomeAdd03',
        'city': 'ssmHomeCity',
        'postcode': 'ssmHomePostal',
        'state': 'ssmHomeState',
        'gender': 'ssmGender',
        'race': 'ssmRace',
        'title': 'ssmTitle'
    },
    'TRIGGER': {
        'CREATE_USER': 'rest_auth.registration.urls',
        # 'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    },
    'ASSERTION_URL': 'https://xcessdev.ssm.com.my/#/sso/acs', # Custom URL to validate incoming SAML requests against
    # 'ENTITY_ID': 'SSMProduk', # Populates the Issuer element in authn request
    'NAME_ID_FORMAT': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified', # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': True, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'https://xcessdev.ssm.com.my/#/home' # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

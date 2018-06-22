"""
Core Django settings.

"""

import datetime
import os

import dj_database_url
from django.utils.encoding import smart_str

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Base Django Time Zone Config
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'
USE_TZ = True
USE_I18N = False
USE_L10N = False
USE_I18N = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    'watchung-valley-staging.herokuapp.com',
    str(os.environ.get('ALLOWED_HOST_URL')),
    str(os.environ.get('ALLOWED_HOST_URL2'))
]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
DEFAULT_APPS = [
    'TwinBrooksUser',  # Custom User Model
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

]

THIRD_PARTY_APPS = [
    'easy_thumbnails',
    'filer',
    'mptt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'raven.contrib.django.raven_compat',
    'anymail',
    'autofixture',
    'materializecssform',
    'widget_tweaks',  # Adds functionality to inject classes and such to django forms
    'versatileimagefield',  # ALlows user to upload image and to render crop functions on ti
    'robots',  # Automatically created a robots.txt file based on model rules
    'hijack',  # Allows admin to log in as a certain user, added it to core django project to override tempaltetags
    'compat',  # ^
    'hijack_admin',  # Allows admin to hijack users from the admin
    'easy_select2',
    'django_select2',
    'rangefilter',
    'import_export',
    'django_summernote',
    'opbeat.contrib.django',
     'adminsortable2',
     'ckeditor',
     'ckeditor_uploader'
]

LOCAL_APPS = [
    'TwinBrooksStatic',
    'BaskingRidgeFiles',
    'crispy_forms',


]
CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'TwinBrooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "TwinBrooksStatic", "templates"),
            os.path.join(BASE_DIR, "TwinBrooksStatic", "templates", "common"),
            os.path.join(BASE_DIR, "TwinBrooksStatic", "templates", "app"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

CKEDITOR_CONFIGS = {
    'default': {
           "default": {
        "removePlugins": "stylesheetparser",
    },
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                'uploadwidget',
                  'uploadimage', # the upload image feature
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
    
        ]),
    }
}

WSGI_APPLICATION = 'TwinBrooks.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# HEROKU DATABASE
# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Page Cache-Control
PAGE_CACHE_SECONDS = 6048000

# CACHE Cache-Control
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


# SETTING CUSTOM USER MODEL
AUTH_USER_MODEL = 'TwinBrooksUser.User'

# SITE_ID CONFIG
SITE_ID = 1

# ALL_AUTH SETTINGS
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, "TwinBrooksStatic", "static_only")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "TwinBrooksStatic", "static"),
)

# CONTACT FORM ON FRONT PAGE EMAIL_BACKEND
FRONT_END_CONTACTFORM_EMAIL = str(
    os.environ.get('FRONT_END_CONTACTFORM_EMAIL'))
FRONTEND_PRO_EMAIL = str(
    os.environ.get('FRONTEND_PRO_EMAIL'))

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# CSRF Failure View
CSRF_FAILURE_VIEW = 'TwinBrooks.urls.csrf_failure'

# Amazon Web Services S3 Settings & Configuration
AWS_ACCESS_KEY_ID = str(os.environ.get('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = str(os.environ.get('AWS_SECRET_ACCESS_KEY'))

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'TwinBrooks.utils.MediaRootS3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-us-west-2-697876612843'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

# Django Compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True

ITEM_PURCHASE_EMAILs = ['zacharybedrosian@gmail.com', ]

# Twilio Backend
ACCOUNT_SID = str(os.environ.get('ACCOUNT_SID')),
AUTH_TOKEN = str(os.environ.get('AUTH_TOKEN')),

# Email Backend

# or sendgrid.SendGridBackend, or...
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply.baskingridgecatering@gmail.com'
EMAIL_HOST_PASSWORD = 'Bedrock123'
EMAIL_PORT = 587


# RAVEN_CONFIG
RAVEN_CONFIG = {
    'dsn': str(os.environ.get('SENTRY_PRODUCTION_TOKEN')),

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            # To capture more than ERROR, change to WARNING, INFO, etc.
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# Django Filer Settings
THUMBNAIL_QUALITY = 75
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
THUMBNAIL_SUBDIR = 'versions'

# All Auth Config
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = 'none'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 9986400  # One day in seconds
SESSION_SAVE_EVERY_REQUEST = True
ACCOUNT_SESSION_COOKIE_AGE = 9896400

# Django Celery Config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Django Hijacking Settings
# Where admins are redirected to after hijacking a user
HIJACK_LOGIN_REDIRECT_URL = '/profile/'
# Where admins are redirected to after releasing a user
HIJACK_LOGOUT_REDIRECT_URL = '/club-admin/TwinBrooksUser/user/'
HIJACK_ALLOW_GET_REQUESTS = True

# TwinBrooks Course Condition Password
COURSE_CONDITION_PASSWORD = '#01&^*66e)f+eze6cj3i4s23mp*xwn-wcs%4yl&%(y1ta$jgdm'

# Open Wether Map API Key
OWN_API_KEY = str(os.environ.get('OWN_API_KEY'))

# Summer Note Editor


# PRODUCTION / DEV SPLIT
# DEVELOPMENT ONLY
try:
    from TwinBrooks.local_settings import *

except ImportError:
    pass


# DJANGO DEBUG TOOLBAR CONFIGURATION
if DEBUG:
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    import debug_toolbar
    DEBUG_TOOLBAR = (
        'debug_toolbar',
    )
    INSTALLED_APPS += DEBUG_TOOLBAR

# DEBUG TOOLBAR REQUIRED IP ADDRESS
INTERNAL_IPS = '127.0.0.1'


def _smart_key(key):
    return smart_str(''.join([c for c in key if ord(c) > 32 and ord(c) != 127]))


def make_key(key, key_prefix, version):
    "Truncate all keys to 250 or less and remove control characters"
    return ':'.join([key_prefix, str(version), _smart_key(key)])[:350]

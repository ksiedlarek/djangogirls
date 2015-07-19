import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = os.getenv('DJANGO_DEBUG') != 'FALSE'
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    SECRET_KEY = 'hello!'
else:
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'suit',
    #'suit_redactor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.webdesign',

    'raven.contrib.django.raven_compat',
    'django_date_extensions',
    'storages',
    'markdown_deux',
    'djrill',
    'django_nose',

    'django_countries',
    'crispy_forms',
    'datetimewidget',
    'ckeditor',

    'core',
    'applications',
    'jobs',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangogirls.urls'

WSGI_APPLICATION = 'djangogirls.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='sqlite:///%s' % (os.path.abspath(os.path.join(BASE_DIR, 'db.sqlite3'))))

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'core.context_processors.statistics',
    'django.contrib.messages.context_processors.messages',
)

# Custom

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

AUTH_USER_MODEL = 'core.User'

SUIT_CONFIG = {
    'ADMIN_NAME': 'Django Girls',
    'MENU_ICONS': {
        'jobs': 'icon-list-alt',
    }
}


AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = 'djangogirls'
AWS_HEADERS = {'Cache-Control': 'public, max-age=86400'}
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATIC_URL = '/static/'
    MEDIA_ROOT = 'static/media'
else:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    MEDIA_ROOT = 'staticfiles/media'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATIC_ROOT = 'staticfiles'
MEDIA_URL = '/static/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN')
}

MANDRILL_API_KEY = os.environ.get('MANDRILL_APIKEY')
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "hello@djangogirls.org"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core,applications,jobs',
    '--with-progressive',
]

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": "escape",
    },
    "trusted": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SSLIFY_DISABLE = DEBUG

APPEND_SLASH = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
    		 ['-', 'Bold', 'Italic', 'Underline'],
             ['-', 'Link', 'Unlink'],
             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-'],
        ],
    },
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.megiteam.pl'
EMAIL_PORT = 465
EMAIL_SUBJECT_PREFIX = '[Django Girls]'

JOBS_EMAIL_USER = os.environ.get('JOBS_EMAIL_USER')
JOBS_EMAIL_PASSWORD = os.environ.get('JOBS_EMAIL_PASSWORD')

MEETUPS_EMAIL_USER = os.environ.get('MEETUPS_EMAIL_USER')
MEETUPS_EMAIL_PASSWORD = os.environ.get('MEETUPS_EMAIL_PASSWORD')

try:
    from .local_settings import *
except:
    pass

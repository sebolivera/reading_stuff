import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'reading-stuff.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'readwrite',
    'ckeditor',
    'ckeditor_uploader',
    'django_bootstrap_icons',
    'userauth',
    'compressor'
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
    ]
    
COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler'),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend', 'userauth.backends.EmailBackend']

ROOT_URLCONF = 'reading_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
    os.path.join(BASE_DIR, 'reading_site', 'templates'),],
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

WSGI_APPLICATION = 'reading_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = { # for prod
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bookdb',
#         'USER' :'postgres',
#         'PASSWORD' : '',
#         'HOST' : 'localhost'
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/


EXTRA_LANG_INFO = {
    'zz': {
        'code': 'zz',
        'name': '🏁 Gibberish',
        'name_local': '🏁'+u'\u25CA\u0335\u031B\u0348\u033C\u030A\u030B\u0357\u0300\u030B\u0300\u0304\u0303\u0310\u034B\u0346\u0314\u034B\u0309\u030D\u033F\u035B\u033F\u030E\u0313\u0350\u0350\u033D\u0307\u0351\u0346\u033F\u030E\u0346\u0350\u0358\u0315\u0315\u0315\u0315\u0315\u0360\u035D\u035D\uFE18\u0338\u0322\u0328\u0322\u031B\u031B\u031B\u0353\u0348\u0326\u0339\u0316\u0325\u032A\u0331\u032C\u032E\u0353\u0326\u0323\u0319\u0339\u0320\u0359\u0332\u033C\u032D\u031D\u033A\u034D\u0319\u0356\u034E\u0349\u0330\u0320\u033B\u032C\u0325\u0331\u032A\u0357\u0350\u034C\u0306\u0350\u034A\u030F\u0300\u0309\u0300\u0304\u0309\u0303\u0357\u0301\u0311\u0308\u035B\u0342\u0309\u0350\u0307\u0313\u0312\u0342\u0313\u0305\u0302\u0351\u033F\u030E\u0342\u0350\u030E\u0346\u0358\u0358\u035D\u035D\u035D\u0345\u25EC\u0334\u0328\u0327\u0321\u0322\u0349\u034E\u032E\u032A\u0359\u0329\u0323\u0324\u0329\u0353\u0326\u031C\u0356\u0347\u0324\u031F\u0355\u035A\u034E\u0332\u0319\u0330\u0320\u033C\u0324\u031E\u0319\u0348\u0329\u0354\u032B\u0301\u030C\u0308\u030D\u0311\u0351\u0308\u0310\u0306\u0345\u25FD\u0334\u0328\u0322\u0322\u0322\u0327\u0322\u0322\u034E\u0326\u0349\u0348\u031D\u0332\u0316\u031E\u0359\u032A\u0356\u0318\u035A\u0316\u033B\u0333\u0323\u0333\u0353\u0333\u031F\u032D\u0329\u0347\u0329\u0331\u033B\u033C\u0326\u033C\u0354\u032E\u0318\u0325\u032B\u0325\u0326\u032E\u032B\u0326\u0326\u0348\u034A\u030B\u0309\u030B\u0308\u0301\u0308\u0301\u0306\u0313\u030C\u030E\u0304\u0313\u034B\u0342\u0301\u0308\u0301\u034B\u0313\u035B\u0303\u030C\u0315\u031A\u035C\u035D', # don't try to understand this one, you'll hurt your brain
    },
    'fr':
    {
        'code': 'fr',
        'name': '🤮 Fr*nch',
        'name_local': 'Rançais',
    },
    'en':
    {
        'code': 'en',
        'name': '🇬🇧 English',
        'name_local': '🇬🇧 English'
    }
}

import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('fr', 'French'),
    ('en', 'English'),
    ('zz', 'Gibberish'),
]
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

AUTH_USER_MODEL = 'userauth.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
COMPRESS_ENABLED = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# necessary in prod
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'


CKEDITOR_BASEPATH = os.path.join(BASE_DIR, "ckeditor/")
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True # prevents users from seeing other ppl's uploads
CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_CONFIGS = {

    'default': {
        'height': '100%',
        'width': '100%',
        'toolbarCanCollapse': False,
    },
    'full': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline', 'NumberedList', 'BulletedList',
             '-', 'Outdent', 'Indent', 'Blockquote', 'CreateDiv',
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'TextColor', 'BGColor',
             '-', 'Maximize', 'ShowBlocks',  #'Image' ,
             '-', 'Cut', 'Copy', 'Paste', 'PasteText',
            ],
            ['-', 'SpecialChar',
             '-', 'Source',
            ],
            [
                '-', 'Styles', 'Format', 'Font', 'FontSize'
            ],
            [
                '-', 'BidiLtr', 'BidiRtl'
            ]
        ],
        'width': '100%',
        'height': '600px',
        'toolbarCanCollapse': False,
    },
    'disable': {
        'toolbar': [],
        'width': '100%',
        'height': '600px',
        'toolbarCanCollapse': False,
    },
    'removePlugins' : 'cloudservices'
}
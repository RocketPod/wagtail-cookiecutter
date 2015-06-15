from .base import *  # NOQA

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['WERCKER_MYSQL_DATABASE'],
        'USER': os.environ['WERCKER_MYSQL_USERNAME'],
        'PASSWORD': os.environ['WERCKER_MYSQL_PASSWORD'],
        'HOST': os.environ['WERCKER_MYSQL_HOST'],
        'PORT': os.environ['WERCKER_MYSQL_PORT'],
    }
}

SENDFILE_BACKEND = 'sendfile.backends.development'

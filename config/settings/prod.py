from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3.34.85.206']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'it:S#i&R.:J1J}pFKxu#;4LF96VH,1U}',
        'HOST': 'ls-e3071c3a6f3ebe97c2c12be5fff717d078aed22a.cygxbr5gvl3t.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
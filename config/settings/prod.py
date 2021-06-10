from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3.34.85.206']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('django.db.backends.postgresql_psycopg2', 'django.db.backends.sqlite3'),
        "NAME": os.getenv("DATABASE_NAME", BASE_DIR / 'db.sqlite3'),
        "USER": os.getenv("DATABASE_USER", ''),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", ''),
        "HOST": os.getenv("DATABASE_HOST", None),
        "PORT": os.getenv("DATABASE_PORT", None),        
    }
}
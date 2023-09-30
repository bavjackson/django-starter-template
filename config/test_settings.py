from .settings import *

DATABASES = {
    'default': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

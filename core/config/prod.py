from core.config.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lf_qe0+^$+c)_0&vcy@c%u09!b@_m3os%j$1h8#n(kec&mz_j1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restaurantdb',
        'USER': 'devadmin',
        'PASSWORD': 'Ninja6708',
        'HOST': 'db',
        'PORT': '5432'
    }
}
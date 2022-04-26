import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-vpi)h^p6+6-$_)zb1_nyo1=@#&(du69*!dz3zx(suut&sz(ek1'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'article_feed',
      'USER':'user_db',
      'PASSWORD':'12345',
      'HOST':'localhost',
      'PORT':'5432',
   }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
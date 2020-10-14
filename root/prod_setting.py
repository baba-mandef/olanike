from root.settings import *
import dj_database_url

DEBUG = False
TEMPLATES_DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['olanike.herokuapp.com']
DATABASES['default'] = dj_database_url.config()

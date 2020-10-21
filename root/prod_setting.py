from root.settings import *
import dj_database_url

DEBUG = True
TEMPLATES_DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['olanike.herokuapp.com']
DATABASES['default'] = dj_database_url.config()

CLOUDINARY_STORAGE = {

    'CLOUD_NAME': os.environ.get('CLOUDNAME'),
    'API_KEY': os.environ.get('APIKEY'),
    'API_SECRET': os.environ.get('APISECRET')

}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

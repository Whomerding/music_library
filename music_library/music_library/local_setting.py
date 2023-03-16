# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oxbubx_sl@uu7_-cd06=w#mvf^vpd0r&ar&hvj6%5g7(zdgrbh'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'GUNNhopi66',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
import os, sys
from pathlib import Path
from django.contrib.messages import constants
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Debug com valor True = Modo desenvolvimento
# Debug com valor False = Modo produção
DEBUG = config('DEBUG', default=False, cast=bool)

#ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())
ALLOWED_HOSTS = ['*'] # Aqui fica o dominio, mas comonao tenho vou colocar * pra pegar dominio do heroku

TEMPLATES = os.path.join(BASE_DIR, 'templates')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

sys.path.append(os.path.join(BASE_DIR, "apps"))

INSTALLED_APPS += [
    'site_portifolio.apps.SiteFinansConfig',
    'projetos',
    'produtos',
    'users',
    'api_pix',
    'bootstrapform',

    'rest_framework',
    #'corsheaders',
]

#CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # Colocar esse codigo aqui, no segundo lugar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portifolio_tk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES],
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


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    ]
}

WSGI_APPLICATION = 'portifolio_tk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'rifa_via_pix_db',
        'USER': 'rifa_via_pix',
        'PASSWORD': '@rifapix2022',
        'HOST': 'rifa-via-pix-db.mysql.uhserver.com',
        'PORT': '3306',
    }
}
'''

# INSTALAR A VERSAO DO PYMONGO = pip install pymongo==3.12.3
'''
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT':{
            "host":"mongodb+srv://sistema:sistema2022@main.ylsho.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            "name":"sistema",
            "authMechanism":"SCRAM-SHA-1", # para atlas nuvem db
        }
    }
}
'''

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Alertas do Django (message)
MESSAGE_TAGS = {
constants.DEBUG: 'alert-primary',
constants.ERROR: 'alert-danger',
constants.SUCCESS: 'alert-success',
constants.INFO: 'alert-info',
constants.WARNING: 'alert-warning',
}
"""
Django settings for caffeinecalculator project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$a_$1c*uom=p$jvf(p)3#o793&ulx_s75&--pr7accn5f+j&@z"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# TODO-0-0 Activer le venv et démarrer le serveur backend
# TODO-0-1 Exécuter les migrations et se créer 1 superuser (admin) si ce n'est pas déjà fait
# TODO-0-2 Ajouter l'app caffeinecalculatorapp dans installed apps
# TODO-0-3 Installer les extensions recommandées par le workshop et installer un formatter
# TODO-0-4 Installer les dépendances du projet avec celles pour le dev (--dev)
# et vérifier que toutes les dépendances sont correctement installées à l'aide de pip

# TODO-1-9 Ajouter la bibliothèque rest_framework dans installed apps afin d'avoir accès à
# la browsable API de la bibliothèque
# TODO-1-10 Essayer d'accéder à /api/users/ et vérifier que des données correctes soient bien affichées

# TODO-2-5 Ajouter la bibliothèque "corsheaders" dans installed apps
# et ajouter "corsheaders.middleware.CorsMiddleware" aux middleware et en 1ère position
# et ajouter l'url du frontend (localhost + 127.0.0.1) dans une nouvelle var de type tableau
# nommé CORS_ALLOWED_ORIGINS, la var est à placer après les middleware

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "caffeinecalculatorapp",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

ROOT_URLCONF = "caffeinecalculator.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "caffeinecalculator.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# NOTE: Pagination to control the amount of elements returned by the API
# REST_FRAMEWORK = {
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
#     "PAGE_SIZE": 10,
# }

from pathlib import Path
from decouple import config, UndefinedValueError
import dj_database_url
import django_heroku
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = config("DEBUG", default=True, cast=bool)

try:
    SECRET_KEY = config("SECRET_KEY")
except UndefinedValueError:
    if not DEBUG:
        raise RuntimeError("Missing SECRET_KEY environment variable")
    else:
        SECRET_KEY = "----secret-dev-key----"

ALLOWED_HOSTS = ["levensfilosofie.nu", "www.levensfilosofie.nu", "localhost"]

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    "annonces.apps.AnnoncesConfig",
    "leden.apps.LedenConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "django_summernote",
    "cloudinary",
    "tailwind",
    "theme",
    "django_browser_reload",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = "levensfilosofie.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "levensfilosofie" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "theme.context_processors.tailwind_classes",
            ],
        },
    },
]

WSGI_APPLICATION = "levensfilosofie.wsgi.application"


try:
    config("DATABASE_URL")
except UndefinedValueError:
    DATABASE_DEFAULT_CONFIG = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db" / "db.sqlite3",
    }
else:
    DATABASE_DEFAULT_CONFIG = dj_database_url.config(conn_max_age=600, ssl_require=True)

DATABASES = {"default": DATABASE_DEFAULT_CONFIG}


SUMMERNOTE_CONFIG = {
    "summernote": {
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        "toolbar": [
            ["style", ["bold", "italic", "underline", "clear"]],
            ["font", ["strikethrough", "superscript", "subscript"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["link", ["linkDialogShow", "unlink"]],
            ["table", ["table"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ]
    },
    "disable_attachment": True,
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "nl"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = (BASE_DIR / "static",)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

if not DEBUG:
    COMPRESS_OFFLINE = True
    LIBSASS_OUTPUT_STYLE = "compressed"

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": config("CLOUDINARY_API_KEY"),
    "API_SECRET": config("CLOUDINARY_API_SECRET"),
}
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_CLASSES = {
    "prose": "prose prose-lg prose-stone prose-headings:font-heading mx-auto",
    "background": "bg-sundance-50",
}

cloudinary.config(**{k.lower(): v for k, v in CLOUDINARY_STORAGE.items()})

django_heroku.settings(locals())

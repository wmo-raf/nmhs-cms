from .base import *

if os.path.exists(os.path.join(BASE_DIR, '.env')):
    # reading .env file
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5=&i=f&w$_2=ktbhw43anl(uxgue*-i23r!1uibrh9l7-$q-1#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

# Disable caching in dev
WAGTAIL_CACHE = False

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.styleguide',
    # 'debug_toolbar',
]

# MIDDLEWARE = MIDDLEWARE + [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]


# INSTALLED_APPS = INSTALLED_APPS + [
#     'debug_toolbar'
# ]

# MIDDLEWARE = MIDDLEWARE+ [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

SHOW_TOOLBAR_CALLBACK=False
SHOW_COLLAPSED=False


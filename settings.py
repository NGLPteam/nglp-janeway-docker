import environ

from core import janeway_global_settings

env = environ.Env()

MERGEABLE_SETTINGS = set()

DATABASES = {
    "default": env.db("DATABASE_URL", 'sqlite:////srv/janeway/db.sqlite3'),
}

MIDDLEWARE_CLASSES = list(janeway_global_settings.MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.insert(
    MIDDLEWARE_CLASSES.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

EMAIL_BACKEND = env.str('EMAIL_BACKEND', default=janeway_global_settings.EMAIL_BACKEND)
EMAIL_HOST = env.str('EMAIL_HOST', default=janeway_global_settings.EMAIL_HOST)
EMAIL_PORT = env.int('EMAIL_PORT', default=25)
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default=janeway_global_settings.EMAIL_HOST_USER)
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default=janeway_global_settings.EMAIL_HOST_PASSWORD)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=janeway_global_settings.EMAIL_USE_TLS)
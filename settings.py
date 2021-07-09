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

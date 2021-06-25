# A Docker image for Janeway in the context of NGLP

This builds a Docker image for Janeway based on either a tag or branch.

The image uses gunicorn as a production-ready WSGI server, and whitenoise to
serve static files.

Additional Django settings are copied in using the `settings.py` file, and
fixtures are used to instantiate a press.

The `bootstrap.sh` script should take care of building and running the image,
and then running database migrations and loading the fixtures.

#!/bin/sh

docker-compose up -d --build


docker-compose exec janeway python /srv/janeway/src/manage.py migrate

(
  cd fixtures ;
  find . -name '*.yaml' -exec \
    docker-compose exec janeway python /srv/janeway/src/manage.py loaddata /srv/janeway/fixtures/{} \;
)

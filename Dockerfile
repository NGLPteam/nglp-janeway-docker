FROM python:3.8

WORKDIR /srv/janeway

# 'master' or e.g. 'v1.3.9'
ENV JANEWAY_REF=master
# 'head' or 'tag'
ENV JANEWAY_REF_TYPE=head

ENV PYTHONPATH=/srv/janeway/src

RUN pip install gunicorn whitenoise django-environ PyYAML

ADD https://raw.githubusercontent.com/BirkbeckCTP/janeway/${JANEWAY_REF}/requirements.txt /srv/janeway/requirements.txt

RUN pip install -r /srv/janeway/requirements.txt

RUN wget https://github.com/BirkbeckCTP/janeway/archive/refs/${JANEWAY_REF_TYPE}s/${JANEWAY_REF}.tar.gz -O /srv/janeway.tar.gz \
    && tar -xf /srv/janeway.tar.gz --strip-components=1 -C /srv/janeway \
    && rm /srv/janeway.tar.gz

COPY settings.py /srv/janeway/src/core/settings.py

RUN python /srv/janeway/src/manage.py collectstatic --no-input

RUN mkdir /srv/janeway/fixtures/
VOLUME /srv/janeway/fixtures/

EXPOSE 8000

ENTRYPOINT ["gunicorn", "core.wsgi:application"]
CMD ["-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]

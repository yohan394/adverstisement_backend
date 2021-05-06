FROM python:3.8-alpine

# [SET-PATH] #
ENV PATH="/scripts:${PATH}"

# [REQUIREMENTS-COPY]
COPY ./requirements.txt /requirements.txt

# [APP_DIRECTORY-COPY]
RUN mkdir /app
COPY ./app /app
WORKDIR /app

# [ADD-STATIC-VOLUMES]
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# [USER-ADDITION] : add user & give ownership to static directories.
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

# [USER-SETTING] : user could be chosen as <non-root>. But if so, manage.py migrate could have ownership problems.
USER root

# [MY-SQL-RELATED] :
RUN apk add --update mysql-client
RUN apk update \
    # MARIADB
    && apk add --virtual build_deps python3-dev gcc musl-dev \
    && apk add --no-cache mariadb-dev \
     # ETC [=channels/Django/uWSGI/gunicorn/cryptography/channels_redis] :
    && apk add --virtual .tmp libc-dev linux-headers libressl-dev libffi-dev libffi \
    # PILLOW :
    && apk add --virtual --no-cache .tmp jpeg-dev zlib-dev build-base \
    && pip install -r /requirements.txt

# [SCRIPT-DIRECTORY-COPY]
COPY ./scripts /scripts

# [BASH-SCRIPTS] :
#   1. collectstatic + uwsgi initialize
RUN chmod +x /scripts/*

# [TMP-DIRECTORIES-DELETE]
RUN apk del .tmp
RUN apk del build_deps

CMD ["entrypoint.sh"]


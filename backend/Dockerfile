FROM python:3.6-slim AS backend

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

ENV CUBAVSCOVID__DJANGO_SECRET_KEY ${CUBAVSCOVID__DJANGO_SECRET_KEY}
ENV CUBAVSCOVID__DJANGO_HOSTNAME ${CUBAVSCOVID__DJANGO_HOSTNAME}
ENV CUBAVSCOVID__DJANGO_PRODUCTION_STATIC_ROOT ${CUBAVSCOVID__DJANGO_PRODUCTION_STATIC_ROOT}
ENV CUBAVSCOVID__DJANGO_PRODUCTION_MEDIA_ROOT ${CUBAVSCOVID__DJANGO_PRODUCTION_MEDIA_ROOT}

RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN mkdir -p /backend
ADD . /backend
WORKDIR /backend

RUN pip3 install poetry
RUN python3 -m poetry install
RUN chmod +x prod.py

CMD chmod +x prod.py; \
    poetry run ./prod.py makemigrations core; \
    poetry run ./prod.py makemigrations uploads; \
    poetry run ./prod.py migrate; \
    poetry run ./prod.py collectstatic --no-input; \
    poetry run daphne -b 0.0.0.0 -p 8000 backend.asgi:application;

EXPOSE 8000

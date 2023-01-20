FROM python:3.10.9-alpine
LABEL maintainer="DazzioD2G"

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
COPY . .
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt && \
    ls &&\
    rm -rf /tmp &&\
    adduser --disabled-password \
    --no-create-home \
    django-user

USER django-user


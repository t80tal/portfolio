FROM python:3.11.9-alpine3.20
LABEL maintainer="https://github.com/t80tal"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements-dev.txt /tmp/requirements-dev.txt
COPY ./api /api
WORKDIR /api
EXPOSE 8000
ARG ENV=development
RUN python -m venv /opt/venv && \
  /opt/venv/bin/pip install --upgrade pip && \
  /opt/venv/bin/pip install -r /tmp/requirements.txt && \
  if [ $ENV = "development" ]; then /opt/venv/bin/pip install -r /tmp/requirements-dev.txt; fi && \
  rm -rf /tmp && \
  adduser \
  --disabled-password \
  --no-create-home \
  django-user

ENV PATH="/opt/venv/bin:$PATH"

USER django-user

FROM node:22-alpine
LABEL maintainer="https://github.com/t80tal"

COPY . /web
WORKDIR /web
RUN npm install && \
    adduser \
    --disabled-password \
    --no-create-home \
    react-user && \
    chown -R react-user:react-user /web

ENV PATH="/web/node_modules/.bin:$PATH"

USER react-user

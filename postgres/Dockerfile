
FROM postgres:15.2-alpine

ENV POSTGRES_USER nhatnguyen1011997
ENV POSTGRES_PASSWORD 1011997
ENV POSTGRES_DB database

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 5434

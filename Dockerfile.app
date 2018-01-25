FROM registry.laboratorium.ee/mhp/mhp-base:latest
ADD . /code/ 
RUN cd /code/ && DJANGO_DATABASE_URL=None DJANGO_SECRET_KEY=None python3 manage.py compress --force
LABEL maintainer="pomoc@adminotaur.pl"

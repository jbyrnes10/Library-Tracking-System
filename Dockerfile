FROM python:latest
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt
RUN apt-get install libmysqlclient-dev

RUN mkdir /var/djangoproject/media_library

WORKDIR /var/djangoproject/media_library


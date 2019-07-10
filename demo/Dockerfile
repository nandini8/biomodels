FROM python:3.6
EXPOSE 8000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt 

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE demo.settings

ADD . /usr/src/app
RUN echo "$PWD"
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8000"]


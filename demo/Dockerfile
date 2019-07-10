FROM python:3.6
EXPOSE 8000

RUN mkdir -p /usr/src/python
COPY requirements.txt /usr/src/requirements.txt

WORKDIR /usr/src/python
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE demo.settings.local

WORKDIR /usr/src/app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
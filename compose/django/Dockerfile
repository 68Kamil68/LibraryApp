FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends libpq-dev python3-dev gcc

WORKDIR /app/

COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/django/wait-for-it.sh ./wait-for-it.sh
COPY ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . /app

CMD ["python3", "manage.py", "runserver_plus", "0.0.0.0:8000"]

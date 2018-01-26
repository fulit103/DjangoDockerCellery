FROM python:2.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 run_celery.sh

RUN chmod 777 run.sh

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
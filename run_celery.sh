#!/bin/sh

#celery -A mysite worker -l info &
celery -A mysite beat -l info &
python run_celery.py 

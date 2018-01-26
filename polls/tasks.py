from celery.decorators import task

from django.core.mail import send_mail

@task(name="sum_two_numbers")
def add(x, y):
    send_mail("esto funciona! %s + %s " %( x, y ), "This will get sent through Mailgun", "Anymail Sender <from@example.com>", ["jtoro@tecmovin.com"])
    return x + y
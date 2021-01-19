import email
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from django.template.loader import render_to_string


@shared_task
def send_email_task(email):
    template = render_to_string('store/email_template.html')

    print(email)
    send_mail('Thanks for shopping with us',
    template,
    settings.EMAIL_HOST_USER,
    [email])

    return None


      
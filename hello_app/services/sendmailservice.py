from django.core.mail import send_mail
from django.conf import settings


def sendmail(subject:str,message:str,send_to:str):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [send_to])
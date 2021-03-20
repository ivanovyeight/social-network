from celery import shared_task
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


@shared_task
def add():
    return "TASK"

@shared_task
def activation_email(username, email):
    username = username.encode("utf-8")
    activation_token = urlsafe_base64_encode(username)
    
    return send_mail(
        "Welcome! Activate your account. [CELERY]",
        f"Hello! To activate your account follow this link: http://localhost:8080/activate?token={activation_token}",
        'admin@socialnetwork.com',
        [email],
        fail_silently=False
    )

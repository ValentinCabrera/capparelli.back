from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(subject, message, recipient_list):
    from_email = 'valentincabrera2003@gmail.com'
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

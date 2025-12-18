from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f'New User created: {instance.username}')

        subject = 'Welcome to Django Backend'
        message = f"""
        Hi {instance.username},
This is a simple message being sent to the new user in account for the new login,
we welcome you to our DJANGO BACKEND with pleasure.
"""     
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send(fail_silently=False)

        print('Welcome email sent Successfully.')
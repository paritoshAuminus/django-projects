from django.core.mail import send_mail, EmailMessage, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string

# Simple email here (send_mail).
def send_email(request):
    subject = 'Paritosh test email'
    message = 'Message here'

    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['somemail@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent')

# Email with html template as the content here (EmailMessage).
def send_email(request):
    subject = 'Paritosh Test Email'
    message = render_to_string('blog/email_template.html', {
        'username': 'TestUsername',
        'context': 'Context coming from key \'context\''
    })
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['somemail@gmail.com']

    email = EmailMessage(
        subject,
        message,
        from_email,
        recipient_list
        )
    
    email.content_subtype = 'html'  # main content is not text/html
    email.send()

    return HttpResponse('Email sent successfully!!')

# Bulk email with send_mass_mail
# LIMITATION - It cannot send templates as messages, only text

def send_email(request):
    message1 = ('subject', 'message', settings.EMAIL_HOST_USER, ['somemail1@gmail.com'])
    message2 = ('subject', 'message', settings.EMAIL_HOST_USER, ['somemail2@gmail.com'])
    message3 = ('subject', 'message', settings.EMAIL_HOST_USER, ['somemail3@gmail.com'])

    send_mass_mail((message1, message2, message3), fail_silently=True)
    return HttpResponse('Emails sent successfully.')

# Send email with EmailMultiAlternatives
# ADVANTAGE - Send multiple emails and with attachments like html, pdf, image etc
def send_email(request):
    mail = EmailMultiAlternatives('Subject', 'message', settings.EMAIL_HOST_USER, ['somemail1@gmail.com', 'somemail2@gmail.com'])
    mail.attach_alternative('blog/email_template.html', 'text/html')
    mail.send(fail_silently=True)

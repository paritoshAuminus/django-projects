from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string

# Simple email here (send_mail).
# def send_email(request):
#     subject = 'Paritosh test email'
#     message = 'Message here'

#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = ['auminuskun@gmail.com']

#     send_mail(subject, message, from_email, recipient_list)

#     return HttpResponse('Email sent')

# Email with html template as the content here (EmailMessage).
def send_email(request):
    subject = 'Paritosh Test Email'
    message = render_to_string('blog/email_template.html', {
        'username': 'TestUsername',
        'context': 'Context coming from key \'context\''
    })
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['gpic2794sumit8a1@gmail.com', 'auminuskun@gmail.com']

    email = EmailMessage(
        subject,
        message,
        from_email,
        recipient_list
        )
    
    email.content_subtype = 'html'  # main content is not text/html
    # email.send()      -------------->> PLEASE UNCOMMENT THIS TO SEE ACTION

    return HttpResponse('Email sent successfully!!')
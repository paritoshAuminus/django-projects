from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def contact_form(request):
    return render(request, 'contact/contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            models.Contact.objects.create(name=name, message=message)
            return HttpResponse(f'Thankyou {name}, for your message')
        
        else:
            return HttpResponse('Please provide both name and message.')
        
    return redirect('contact_form')
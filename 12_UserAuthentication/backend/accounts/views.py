from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import RegistrationForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User registered succesfully')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the following error')
    else:
        form = RegistrationForm()  
    return render(request, 'register.html', {'form': form})

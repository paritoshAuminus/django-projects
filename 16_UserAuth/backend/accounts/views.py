from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileForm
from .models import Profile


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration complete, user logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed, please try again.')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded successfully!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error uploading file picture')
    else:
        form = ProfileForm()
    
    return render(request, 'accounts/upload_profile.html', {'form': form}) 

def view_profile(request):
    profile = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profile': profile})

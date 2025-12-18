from django.shortcuts import render
from django.core.cache import cache, caches
from .models import YoutubeUser, UserProfile

# Create your views here.
def users_list(request):
    users = cache.get('users_data')     # Trying to get data from cache (users_data is just a unique name, not related to any variable) 
    if not users:
        print('Cache miss: Fetching data from database')
        users = YoutubeUser.objects.all()
        cache.set('users_data', users, timeout=300) # Cache data for 300 seconds
    else:
        print('Cache hit: Fetching data from cache')

    return render(request, 'user_list.html', {'users': users}) 


def profile_view(request):
    file_cache = caches['filebase']  # <-- use file-based cache
    profiles = file_cache.get('profiles_data')

    if profiles is None:
        print('Cache miss: Fetching data from database')
        profiles = list(UserProfile.objects.all())  # convert queryset!
        file_cache.set('profiles_data', profiles, timeout=300)
    else:
        print('Cache hit: Fetching data from my_cache :: filebase')

    return render(request, 'user_profile.html', {'profiles': profiles})

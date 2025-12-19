from django.shortcuts import render
from django.core.cache import cache, caches
from .models import YoutubeUser, UserProfile, VideoCount, Blog
from django.views.decorators.cache import cache_page

# Create your views here.
# Regular memory caching
def users_list(request):
    users = cache.get('users_data')     # Trying to get data from cache (users_data is just a unique name, not related to any variable) 
    if not users:
        print('Cache miss: Fetching data from database')
        users = YoutubeUser.objects.all()
        cache.set('users_data', users, timeout=300) # Cache data for 300 seconds
    else:
        print('Cache hit: Fetching data from cache')

    return render(request, 'user_list.html', {'users': users}) 


# file based caching
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

# filebased caching + perview caching technique
@cache_page(30, cache='perviewFilebase')     # cache the view for 30 seconds
def video_view(request):
    print('video_view :: no cache yet :: Fetching data from the database')
    videos = VideoCount.objects.all()

    return render(request, 'video.html', {'videos': videos})

# NOTE: For Template fragment cache navigate to ..(project root)/backend/youtube/templates/user_list.html

# database caching
def blog_view(request):
    db_cache = caches['databaseCache']
    blogs = db_cache.get('blogs')

    if not blogs:
        print('Database cache miss :: querying database for blogs')
        blogs = Blog.objects.all()
        db_cache.set('blogs', blogs, 30)
    else:
        print('Database cache hit :: fetching data from cache')

    return render(request, 'blog.html', {'blogs': blogs})

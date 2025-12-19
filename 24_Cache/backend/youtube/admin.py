from django.contrib import admin
from .models import YoutubeUser, UserProfile, VideoCount, Blog
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear User Cache')
def clear_user_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request, 'Users Cache deleted successfully.')

# Register your models here.
@admin.register(YoutubeUser)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subscribers']
    actions = [clear_user_cache]

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'friends']

@admin.register(VideoCount)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'views']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']
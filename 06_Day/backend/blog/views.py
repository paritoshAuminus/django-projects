from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogpost(request, blog_id):
    return HttpResponse(f'This is the blog number {blog_id}')

def user_profile(request, user_id):
    return HttpResponse(f'This is user {user_id}')

def blog_by_year(request, year):
    return HttpResponse(f'The year of the post is {year}')

# def article_details(request, year, month):
#     return HttpResponse(f'The article was published on {year} - {month}')

def article_details(request, **kwargs):
    return HttpResponse(f'The article was published on f{kwargs}')

def home_page(request):
    return render(request, 'blog/home.html')

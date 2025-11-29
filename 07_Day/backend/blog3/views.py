from django.shortcuts import render
import datetime

# Create your views here.
def blog_list(request):

    blogs = [
        {'title': 'Django Basics', 'is_featured': True, 'author': 'Paritosh'},
        {'title': 'Django Advanced', 'is_featured': False, 'author': 'John Doe'},
        {'title': 'Django REST_framework', 'is_featured': False, 'author': 'Kevin Magnusson'}
    ]

    context = {
        'blogs': blogs,
        'today': datetime.datetime.now(),
        'html_code': '<h1>Welcome to my blog</h1>'
    }
    return render(request, 'blog3/blog3.html', context)
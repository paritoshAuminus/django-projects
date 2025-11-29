from django.shortcuts import render
import datetime

# Create your views here.
def blog_details(request):
    post = {
        'title': 'My second template post',
        'description': 'Django is a high level frameword',
        'author': None,
        'created_at': datetime.datetime(2025, 12, 10, 22),
        'comment_count_6': 6,
        'comment_count_1': 1,
        'tags': ['Django', 'python', 'web development'],
        'price': 60,
        'number': 7,
    }
    return render(request, 'blog2/blog2.html', {'post': post})
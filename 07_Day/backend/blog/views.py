from django.shortcuts import render
import datetime
# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': 'Paritosh',
        'age': 28,
        'skill': ['python', 'django', 'React JS'],
        'user': User('Rajat', 30),
        'blog': {
            'title': 'Django template intro',
            'content': '<b>This is the content of the blogpost</b>',
            'created_at': datetime.datetime(2025, 8, 18, 10, 30),
            'author': {
                'name': 'Rajat'
            }
        },
        'empty_value': None
    }

    return render(request, 'blog/home.html', context)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'paritosh'
    request.session['course'] = 'Django full course'
    return HttpResponse('Session data saved successfully')

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f'Welcome {username}, you are enrolled in this course: {course}')

def delete_session(request):
    # Manually deleting all data
    # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse('Session data deleted successfully.')

    # Deleting all sessions with one command
    request.session.flush()
    return HttpResponse('All session data deleted successfully.')
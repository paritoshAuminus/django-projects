from django.shortcuts import render
from django.http import HttpResponse

# Create your sessions views here.
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


# Store all your cookies views here
def set_cookies(request):
    response = HttpResponse('Cookies created successfully!')
    response.set_cookie('theme', 'dark', max_age=60*60*24)      # max_age=One_day
    response.set_cookie('color', 'magenta', max_age=60*60*24)
    return response

def get_cookies(request):
    theme = request.COOKIES.get('theme', 'No theme set')
    color = request.COOKIES.get('color', 'No color set')
    return HttpResponse(f'The theme is {theme} and the color is {color}')

def delete_cookies(request):
    response = HttpResponse('Cookies deleted succesfully.')
    response.delete_cookie('theme')
    response.delete_cookie('color')
    return response
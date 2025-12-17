## Storing Sessions and Cookies

* HTTP is a stateless protocol, hence it doesn't care who or what the user or client is.
* Server doesn't store unnecessary data like requests and response records.
* To store valued data, sessions and cookies are used.

### Comparison Between Sessions and Cookies

| **Sessions**                                                | **Cookies**                                                     |
| ----------------------------------------------------------- | --------------------------------------------------------------- |
| Session data is stored in server                            | Cookies are stored in browser                                   |
| Sessions can have as much storage as the database           | Cookies have limited storage (localstorage of the browser ~5kb) |
| Sessions are used to store sensitive data (eg - Session id) | Cookies are used to store general data (eg - theme)             |

---

## Syntax

### Working with Sessions

```bash
# Create your sessions views here.
def set_session(request):
    request.session['username'] = 'paritosh'
    request.session['course'] = 'Django full course'
    return HttpResponse('Session data saved successfully')  # Response body

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f'Welcome {username}, you are enrolled in this course: {course}')   # Response body

def delete_session(request):
    # Manually deleting all data
    try:
        del request.session['username']
        del request.session['course']
    except KeyError:
        pass
    # return HttpResponse('Session data deleted successfully.')

    # Deleting all sessions with one command
    request.session.flush()
    return HttpResponse('All session data deleted successfully.')
```

### Working with Cookies

```bash
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
```
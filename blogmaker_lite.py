from django.urls import path
from pathlib import Path
import os
import django
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.shortcuts import render

#load Settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

'''
view function: A function that defines what will be displayed when a request is passed from client to a server
Notes: This is the same thing that I had done in while working with the bottle framework.
'''
def index(request):
    return render(request, "index.html") # render is used for rendering the content  ie adding the content with inserting information. As opposed to just showing the template(HTTPResponse)

'''
urlpattern defines the urls that the client is passing to the server along with the map of the url with the view function.
'''
urlpatterns = [
path("", index)
]

'''
WSGI: Web Server Gateway Interface. It handles the requests that come in and builds appropriate response that could be returned
'''
application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()

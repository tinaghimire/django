Django (Part - 1)

virtualenv djan --- Create a virtual environment named djan
source djan/bin/activate --- Activate the virtual environment
git init --- Initialize a git repository
pip3 install django --- Install django
django-admin startproject backend --- Start a project named backend
ls
---contains file " backend  djan "
code .

Before running the command including manage.py 
cd <projectname>
ls 
to check if you are inside the folder containing manage.py file
python manage.py runserver --- to run server
python manage.py startapp hello --- create a django app within the project backend

#inside settings.py
add 'hello' app in INSTALLED_APPS list 

#inside hello views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world!")

#inside hello create urls.py(separate urls links for separate apps for simplicity)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

#inside backend project urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls"))
]

Then run the server using
python manage.py runserver

To add more contents

#inside hello views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def greet(request):
    return HttpResponse("Nice to meet you")

#inside hello create urls.py(separate urls links >
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("greet/", views.greet, name="greet"), 
]

#inside hello views.py
from django.http import HttpResponse

def callname(request):
    # return HttpResponse(f"Hello, {name}!")
    return HttpResponse(f"Hello, {name.capitalize()}!")


#inside hello create urls.py(separate urls links >
from django.urls import path
from . import views

urlpatterns = [
    ....,
    path("<str:name>", views.callname, name="callname"),
]

Note: If you create http://127.0.0.1:8000/hello/prerit
it will create
	# Hello, prerit
	Hello, Prerit -- Capitalize the name

#inside hello views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, It's me Kristina!")

# def greet(request):
#     return HttpResponse("Nice to meet you")

def index(request):
    return render(request, "hello/index.html")

def callname(request, name):
    # return HttpResponse(f"Hello, {name}")
    return HttpResponse(f"Hello, {name.capitalize()}!")


#inside hello urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("greet", views.greet, name="greet"),
    path("<str:name>", views.callname, name="callname"),
]

Create a folder named templates inside hello
and create a file named "hello/index.html" -- using directory name hello makes it easier to differentiate the files having many index.html file

Django (Part - 2)

source djan/bin/activate --- Activate the virtual environment
django-admin startproject backend2 --- Start a project named backend2
ls
---contains file " backend  djan "

code .

Before running the command including manage.py 
cd <projectname>
ls 
to check if you are inside the folder containing manage.py file
python manage.py runserver --- to run server
python manage.py startapp hello --- create a django app within the project backend

#inside settings.py
add 'hello' app in INSTALLED_APPS list 

#inside hello views.py
from django.http import HttpResponse
def index(request, name):
    return render(request, "hello/index.html", {"name": name.capitalize()})

#inside hello create urls.py(separate urls links for separate apps for simplicity)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

#inside backend project urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls"))
]

Then run the server using
python manage.py runserver

New year app
create a new app newyear

#inside newyear views.py
import datetime

# Create your views here.
def year(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html",{
        "newyear": now.month == 1 and now.day == 1
        })
        
#inside newyear/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>newyear</title>
</head>
<body>
    {% if newyear %}
        <h1>Yes</h1>
    {% else %}
        <h1>No</h1>
    {% endif %}
</body>
</html>

Then run the server





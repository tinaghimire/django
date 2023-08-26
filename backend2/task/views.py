from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse  #Get back to page

tasks = ["foo", "bar", "baz"]  #Global variable

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) 
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html", {
                "form" : form
            })

    return render(request, "task/add.html", {
        "form" : NewTaskForm()
    })

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "task/index.html", {
        # "tasks":tasks
        "tasks" : request.session["tasks"]
    })


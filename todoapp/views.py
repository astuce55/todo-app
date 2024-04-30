from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def home(request):
    all_task = task.objects.all()
    task_tab = []
    for my_task in all_task:
        task_tab.append(my_task.Title)

    return render(request, "index.html", {'tasks': all_task})

def add_task(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        Complete = False
        Deleted = False
    
        tache = task(Title)
        tache.save()

        response = {
            'success': True,
        }

        return JsonResponse(response)
    
    else:
        # Handle invalid request method (e.g., GET)
        return render(request, 'add_task.html') # Replace with your actual template


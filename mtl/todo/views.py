from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Task

# Create your views here.


def home(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(title=title, desc=desc)
        ins.save()
        print("saved successfully")


    return render(request, 'todo/home.html')

def task(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'todo/task.html', context)





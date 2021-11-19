from django.shortcuts import render
from testapp.models import Task
from testapp.forms import TaskForm
from django.http import HttpResponseRedirect

# Create your views here.

def HomeView(request):

    success = False
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        print(name,desc)
        ins = Task(name=name,desc=desc)
        ins.save()

        success = True
        return render (request,'testapp/home.html',{'success':success})

    return render (request,'testapp/home.html',{'success':success})


def TaskListView(request):
    tasks = Task.objects.all()
    return render (request,'testapp/taskList.html',{'tasks':tasks})

def TaskEditView(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)

    if request.method == 'POST':

        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ('/')

    return render (request,'testapp/taskUpdate.html',{'form':form})



def TaskDeleteView(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect ('/')

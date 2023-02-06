from django.shortcuts import render
from app.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):

    if request.method == "POST":
        task = request.POST.get('task')
        date = request.POST.get('date')
        desc = request.POST.get('desc')

        todo = Todo(task=task, date=date, desc=desc)
        todo.save()
        return HttpResponseRedirect("/")

    todo_item = Todo.objects.all()
    context = {"todo_items" : todo_item}
    return render(request, 'To do list.html', context)

def edit(request, todo_id):
    if request.method == "POST":
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        temp = Todo.objects.get(id = todo_id)
        temp.task = task
        temp.desc = desc
        temp.date = date
        temp.save()
        return HttpResponseRedirect("/")

    
    todo_item = Todo.objects.get(id=todo_id)
    context = {"todo_item" : todo_item}
    return render(request, 'Edit-Page.html',context)

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

def todo_list(request):
    todo = Todo.objects.all()
    return render(request, "index.html", {'todo': todo})

def create_todo(request):
    if request.method == "POST":
        title = request.POST.all("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        Todo.objects.create(title=title, description=description, due_date=due_date)
        return redirect('todo_list')
    return render(request, 'create_todo.html')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.due_date = request.POST.get("due_date")
        todo.save()
        return redirect('todo_list')
    return render(request, 'edit_todo.html', {'todo': todo})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'confirm_delete.html', {'todo': todo})



def complete_todo(request,todo_id):
    todo=todo.object.get(id=todo_id)
    todo.completed= True
    todo.save()
    return redirect('todo_list')
     

from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, user=request.user)
            return redirect('/')

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')

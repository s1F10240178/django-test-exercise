from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from django.utils.dateparse import parse_datetime
from todo.models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_at_str = request.POST.get('due_at')

        due_at = None
        if due_at_str:
            parsed = parse_datetime(due_at_str)
            if parsed:
                due_at = make_aware(parsed) if is_naive(parsed) else parsed

        task = Task(title=title, due_at=due_at)
        task.save()
        return redirect('index')   

    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)

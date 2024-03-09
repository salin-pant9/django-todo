from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def Home(request):
    todo = Todo.objects.all()
    input = request.POST.get('task')
    db = Todo(task=input)
    db.save()
    context = {"tasks": todo}
    return render(request, 'home.html', context)
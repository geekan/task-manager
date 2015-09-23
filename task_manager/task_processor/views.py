from django.shortcuts import render
from django.http import HttpResponse
from models import ImageNeuralTask

# Create your views here.

def index(request):
    tasks = list(ImageNeuralTask.objects.all().values())
    print(tasks)
    return HttpResponse('<br/>'.join([str(task) for task in tasks]))

def add_task(request, *args, **kwargs):
    print(args, kwargs)
    id = args[0] if len(args) else 'test'
    task = ImageNeuralTask(id=id)
    task.save()
    return index(request)

from django.shortcuts import render
from django.http import HttpResponse
from models import ImageNeuralTask

# Create your views here.

def index(request):
    tasks = ImageNeuralTask.objects.all()
    return HttpResponse(str(tasks))

def add_task(request):
    task = ImageNeuralTask(id='test')
    task.commit()
    return HttpResponse('ok')

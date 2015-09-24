from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from models import ImageNeuralTask
from time import strftime, localtime

import logging
import json

l = logging.getLogger(__name__)

def index(request):
    #l.error(__name__)
    tasks = list(ImageNeuralTask.objects.all().values())
    #l.debug(tasks)
    return HttpResponse('<br/>'.join([str(task) for task in tasks]))

@csrf_exempt
def neural_task(request, *args, **kwargs):
    l.warn(args, kwargs, request.POST, request.GET)
    good_paras = ['image_url', 'image_id', 'style_image_path', 'user_id']
    para_dict = {k: request.POST.get(k, '') for k in good_paras}
    para_dict['create_time'] = strftime("%Y-%m-%d %H:%M:%S", localtime())
    para_dict['status'] = 'accepted' if all(para_dict.values()) else 'unaccepted'
    task = ImageNeuralTask(**para_dict)
    task.save()
    return index(request)

def neural_task_json(request, *args, **kwargs):
    return HttpResponse(
        json.dumps(
            list(ImageNeuralTask.objects.filter(status='accepted').values())
        )
    )

@csrf_exempt
def neural_task_clean(request, *args, **kwargs):
    l.warn(args, kwargs, request.POST, request.GET)
    ImageNeuralTask.objects.filter(Q(image_id='') | Q(user_id='')).delete()
    return index(request)

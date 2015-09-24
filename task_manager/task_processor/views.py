from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from models import ImageNeuralTask
from time import strftime, localtime

import logging

l = logging.getLogger(__name__)

# Create your views here.
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def index(request):
    tasks = list(ImageNeuralTask.objects.all().values())
    l.debug(tasks)
    return HttpResponse('<br/>'.join([str(task) for task in tasks]))

@csrf_exempt
def neural_task(request, *args, **kwargs):
    l.info(args, kwargs, request.POST, request.GET)
    good_paras = ['image_url', 'image_id', 'style_image_path', 'user_id']
    para_dict = {k: request.REQUEST.get(k, '') for k in good_paras}
    para_dict['create_time'] = strftime("%Y-%m-%d %H:%M:%S", localtime())
    task = ImageNeuralTask(**para_dict)
    task.save()
    return index(request)

@csrf_exempt
def neural_task_clean(request, *args, **kwargs):
    l.info(args, kwargs, request.POST, request.GET)
    ImageNeuralTask.objects.filter(Q(image_id='') | Q(user_id='')).delete()
    return index(request)

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.db.models import Q

from models import ImageNeuralTask
from time import strftime, localtime

import logging
import json

l = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'task_processor/index.html'
    context_object_name = 'neural_task_list'

    def get_queryset(self):
        return ImageNeuralTask.objects.order_by('create_time')[:-5]

def index(request):
    return render(
        request,
        'task_processor/index.html',
        {'neural_tasks': json.dumps(list(ImageNeuralTask.objects.all().values()))}
    )

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

def neural_task_set(request):
    good_paras = ['image_id', 'status']
    para_dict = {k: request.GET.get(k, '') for k in good_paras}
    task = ImageNeuralTask.objects.filter(image_id=para_dict['image_id']).update(status=para_dict['status'])
    #return HttpResponse('')
    return index(request)

@csrf_exempt
def neural_task_clean(request, *args, **kwargs):
    l.warn(args, kwargs, request.POST, request.GET)
    ImageNeuralTask.objects.filter(Q(image_id='') | Q(user_id='')).delete()
    return index(request)

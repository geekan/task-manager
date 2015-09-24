from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/(.*)/?$', views.neural_task, name='add_task'),
    url(r'^neural-task/clean/?$', views.neural_task_clean),
    url(r'^neural-task/(.*)/?$', views.neural_task),
]

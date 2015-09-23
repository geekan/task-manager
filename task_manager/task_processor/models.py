from django.db import models

# Create your models here.

class ImageNeuralTask(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    status = models.CharField(max_length=255, default='')
    create_time = models.CharField(max_length=255, default='')
    start_time = models.CharField(max_length=255, default='')
    finish_time = models.CharField(max_length=255, default='')
    image_path = models.CharField(max_length=255, default='')
    image_url = models.CharField(max_length=255, default='')
    style_image = models.CharField(max_length=255, default='')

    #def __str__(self):
    #    return str(self._meta.get_fields())

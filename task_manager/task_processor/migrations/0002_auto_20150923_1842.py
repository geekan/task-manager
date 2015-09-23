# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_processor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageneuraltask',
            old_name='style_image',
            new_name='style_image_path',
        ),
    ]

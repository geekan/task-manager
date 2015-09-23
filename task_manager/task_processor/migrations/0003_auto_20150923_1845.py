# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_processor', '0002_auto_20150923_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageneuraltask',
            old_name='id',
            new_name='image_id',
        ),
    ]

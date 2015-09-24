# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_processor', '0003_auto_20150923_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageneuraltask',
            name='user_id',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]

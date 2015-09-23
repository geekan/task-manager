# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageNeuralTask',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('status', models.CharField(default=b'', max_length=255)),
                ('create_time', models.CharField(default=b'', max_length=255)),
                ('start_time', models.CharField(default=b'', max_length=255)),
                ('finish_time', models.CharField(default=b'', max_length=255)),
                ('image_path', models.CharField(default=b'', max_length=255)),
                ('image_url', models.CharField(default=b'', max_length=255)),
                ('style_image', models.CharField(default=b'', max_length=255)),
            ],
        ),
    ]

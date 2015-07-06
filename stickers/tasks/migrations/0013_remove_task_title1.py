# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_task_title1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title1',
        ),
    ]

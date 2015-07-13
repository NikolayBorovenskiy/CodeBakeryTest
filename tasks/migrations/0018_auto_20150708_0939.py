# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_remove_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
    ]

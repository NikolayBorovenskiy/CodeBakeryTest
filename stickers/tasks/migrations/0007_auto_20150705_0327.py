# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20150705_0108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskitem',
            options={'ordering': ['status']},
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='commontask',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u0434\u0430\u0447\u0430', to='tasks.Task'),
        ),
    ]

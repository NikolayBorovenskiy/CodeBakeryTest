# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20150705_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='commontask',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u0434\u0430\u0447\u0430', to='tasks.Task'),
        ),
    ]

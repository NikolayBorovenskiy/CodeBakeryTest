# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20150706_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title1',
            field=models.CharField(max_length=35, verbose_name='\u0417\u0430\u0433\u043e\u043bd\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]

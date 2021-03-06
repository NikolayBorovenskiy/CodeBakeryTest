# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_auto_20150708_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_finish',
            field=models.DateField(default=datetime.date(2015, 7, 8), help_text=b'\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x80, 09.07.2015', null=True, verbose_name='\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f'),
        ),
    ]

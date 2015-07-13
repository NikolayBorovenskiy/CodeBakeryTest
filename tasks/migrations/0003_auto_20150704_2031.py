# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150704_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='theme',
            field=models.CharField(max_length=10, verbose_name='\u0422\u0435\u043c\u0430', choices=[('\u0440\u0430\u0431\u043e\u0442\u0430', '\u0440\u0430\u0431\u043e\u0442\u0430'), (b'I', '\u043b\u0438\u0447\u043d\u043e\u0435'), (b'F', '\u0441\u0435\u043c\u044c\u044f'), (b'B', '\u043f\u043e\u043a\u0443\u043f\u043a\u0438'), (b'O', '\u0440\u0430\u0437\u043d\u043e\u0435')]),
        ),
    ]

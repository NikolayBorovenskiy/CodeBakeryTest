# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_auto_20150708_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(default=1, max_length=10, verbose_name='\u0426\u0432\u0435\u0442', choices=[(b'red', '\u043a\u0440\u0430\u0441\u043d\u044b\u0439'), (b'yellow', '\u0436\u0435\u043b\u0442\u044b\u0439'), (b'blue', '\u0433\u043e\u043b\u0443\u0431\u043e\u0439'), (b'grey', '\u0441\u0435\u0440\u044b\u0439'), ('viollent', '\u0444\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439')]),
            preserve_default=False,
        ),
    ]

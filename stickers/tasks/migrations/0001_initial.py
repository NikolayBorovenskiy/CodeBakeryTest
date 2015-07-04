# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=35, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('theme', models.CharField(max_length=10, verbose_name='\u0422\u0435\u043c\u0430', choices=[(b'J', '\u0440\u0430\u0431\u043e\u0442\u0430'), (b'I', '\u043b\u0438\u0447\u043d\u043e\u0435'), (b'F', '\u0441\u0435\u043c\u044c\u044f'), (b'B', '\u043f\u043e\u043a\u0443\u043f\u043a\u0438'), (b'O', '\u0440\u0430\u0437\u043d\u043e\u0435')])),
                ('impotent', models.BooleanField(verbose_name='\u0412\u0430\u0436\u043d\u043e\u0435')),
                ('time_public', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('time_finish', models.DateField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discription', models.CharField(max_length=50, verbose_name='\u0427\u0442\u043e \u043d\u0435 \u0437\u0430\u0431\u044b\u0442\u044c?')),
                ('status', models.BooleanField(verbose_name='\u0421\u0434\u0435\u043b\u0430\u043d\u043e!')),
                ('user', models.ForeignKey(to='tasks.Task')),
            ],
        ),
    ]

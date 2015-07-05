#-*- coding: utf-8 -*-
import datetime

from django.utils import timezone
from django.db import models

#from clients.models import Coach


class Task (models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=35, blank=True)
    theme = models.CharField(verbose_name=u'Тема', max_length=10, choices=((u'работа', u'работа'), (u'личное', u'личное'),
                            (u'семья', u'семья'), (u'покупки', u'покупки'), (u'разное', u'разное')), )
    #user = models.ForeignKey(Client)
    impotent = models.BooleanField(verbose_name=u'Важное')
    time_public = models.DateTimeField(verbose_name=u'Время создания', editable=True, auto_now_add=True)
    time_finish = models.DateField(blank=True, null=True, verbose_name=u'Срок выполнения', help_text='например, 09.07.2015')

    class Meta:
        ordering = ['-time_public']

    def __unicode__(self):
        return self.title

class TaskItem (models.Model):
    discription = models.CharField(verbose_name=u'Что не забыть?', max_length=50)
    status = models.BooleanField(verbose_name=u'Сделано!')
    commontask = models.ForeignKey(Task, verbose_name=u'Задача')

    class Meta:
        ordering = ['status']

    def __unicode__(self):
        return self.discription

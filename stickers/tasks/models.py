#-*- coding: utf-8 -*-
import datetime

from datetime import date
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Task (models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=35, blank=True)
    theme = models.CharField(verbose_name=u'Тема', max_length=10, choices=((u'работа', u'работа'), (u'личное', u'личное'),
                            (u'семья', u'семья'), (u'покупки', u'покупки'), (u'разное', u'разное')), )
    user = models.ForeignKey(User, verbose_name=u'Пользователь', null=True, editable=True)
    impotent = models.BooleanField(verbose_name=u'Важное')
    time_public = models.DateTimeField(verbose_name=u'Время создания', editable=True, auto_now_add=True)
    time_finish = models.DateField(blank=True, null=True, verbose_name=u'Срок выполнения', help_text='например, 09.07.2015')


    #Define stickers, which not done
    def not_done(self):
        self.done_status = 'not items'
        if len(self.taskitem_set.all()) != 0:
            if len(self.taskitem_set.all()) == len(self.taskitem_set.all().filter(status=True)):
                self.done_status = 'all done'
            else:
                self.done_status = 'undone'
        return self.done_status


    #fire stikers
    def fire(self):
        if self.time_finish is not None:
            if self.time_finish <= date.today() and self.not_done() is 'undone':
                return True
            else:
                return False
        return False

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

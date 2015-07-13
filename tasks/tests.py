# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from tasks.models import Task, TaskItem


class TaskTest(TestCase):
    def test_desktop(self):
        client = Client()
        #Проверка на случай, когда ни стикер
        response = client.get(reverse('tasks:tasks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Пока нет никаких напоминалок :-(')
        #Создаем пользователя
        user = User.objects.create(username="Codebakery", email='nikolay.borovenskiy@gmail.com')
        #Создаем два стикера
        sticker1 = Task.objects.create(title='Reminder 1', theme='работа', user=user, impotent=True)
        #Создаем 6 новых дел
        for i in xrange(6):
            nem_Item = TaskItem.objects.create(discription=u'Task {}'.format(i+1),
                                               commontask=sticker1,
                                               status=False,
                                               )

        #Проверка, что страница отвечает и стеке выводится правильно
        response = client.get(reverse('tasks:tasks-list'))
        self.assertEqual(response.status_code, 200)
        for sticker in user.task_set.all():
            self.assertContains(response, sticker.title)
            self.assertContains(response, sticker.theme)
            #Проверка, что все уроки курса выводятся
            for item in sticker.taskitem_set.all()[:5]:
                self.assertContains(response, item.discription)

# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView

from tasks.models import Task


# Create task list
class TaskListView(ListView):
    model = Task
    #paginate_by = 8
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        #context['username'] = auth.get_user(self.request).username
        return context

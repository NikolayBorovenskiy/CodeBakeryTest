# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


#Create detail info about task
class TaskDetailView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        task = get_object_or_404(Task, pk = self.kwargs['pk'])
        context['task'] = task
        return context

#Create new sticker
class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy('tasks:tasks-list')
    fields = ['title', 'theme', 'impotent', 'time_finish']

    def get_initial(self):
        return {'theme': u'разное',}

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создать напоминалку"
        #context['username'] = auth.get_user(self.request).username
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Напоминалка созданна. Добавь сколько хочешь задач на нее!')
        return super(TaskCreateView, self).form_valid(form)




# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tasks.models import Task, TaskItem


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
        messages.success(self.request, u'Напоминалка {} созданна. Добавь сколько хочешь задач на нее!'.format(self.application.title))
        return super(TaskCreateView, self).form_valid(form)


#Delete current sticker
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks-list')

    def delete(self, request, *args, **kwargs):
        task = super (TaskDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Напоминалка {} удалена'.format(self.object.title))
        return task


#Update current sticker
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'theme', 'impotent', 'time_finish']

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Напоминалка {} изменены'.format(self.application.title))
        return super(TaskUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование напоминалки"
        #context['username'] = auth.get_user(self.request).username
        return context


#Create item of task
class TaskItemCreateView(CreateView):
    model = TaskItem
    #success_url = reverse_lazy('tasks:tasks-list')
    fields = ['discription', 'status', 'commontask']

    def get_initial(self):
        return {'commontask': self.kwargs['pk'],}

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(TaskItemCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создать задачу"
        #context['username'] = auth.get_user(self.request).username
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Задача создана')
        return super(TaskItemCreateView, self).form_valid(form)


#Update current task
class TaskItemUpdateView(UpdateView):
    model = TaskItem
    #success_url = reverse_lazy('tasks:tasks-list')
    fields = ['discription', 'status', 'commontask']


    def get_success_url(self):
        taskitem = get_object_or_404(TaskItem, id = self.kwargs['pk'])
        return reverse_lazy('tasks:task-detail', kwargs={'pk':taskitem.commontask.id})

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Задача изменена')
        return super(TaskItemUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskItemUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование задачи"
        #taskitem = get_object_or_404(TaskItem, id = self.kwargs['id'])
        #context['taskitem'] = taskitem
        #context['username'] = auth.get_user(self.request).username
        return context


#Delete current task
class TaskItemDeleteView(DeleteView):
    model = TaskItem

    def get_success_url(self):
        taskitem = get_object_or_404(TaskItem, id = self.kwargs['pk'])
        return reverse_lazy('tasks:task-detail', kwargs={'pk':taskitem.commontask.id})

    def delete(self, request, *args, **kwargs):
        taskitem = super (TaskItemDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Задача {} удалена'.format(self.object.discription))
        return taskitem

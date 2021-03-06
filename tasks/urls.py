# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from tasks import views

urlpatterns = [
    url(r'^$', views.TaskListView.as_view(), name = 'tasks-list'),
    url(r'^(?P<pk>\d+)$', views.TaskDetailView.as_view(), name = 'task-detail'),
    url(r'^newtask/$', views.TaskCreateView.as_view(), name = 'create-task'),
    url(r'^deletetask/(?P<pk>\d+)$', views.TaskDeleteView.as_view(), name = 'delete-task'),
    url(r'^edittask/(?P<pk>\d+)$', views.TaskUpdateView.as_view(), name = 'edit-task'),
    url(r'^(?P<pk>\d+)/newitem/$', views.TaskItemCreateView.as_view(), name = 'create-item'),
    url(r'^edititem/(?P<pk>\d+)$', views.TaskItemUpdateView.as_view(), name = 'edit-item'),
    url(r'^deleteitem/(?P<pk>\d+)$', views.TaskItemDeleteView.as_view(), name = 'delete-item'),
    #url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name = 'course'),
    #Урлы для редактирование курса
    #url(r'^add/$', views.CourseCreateView.as_view(), name = 'create-course'),
    #url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name = 'edit-course'),
    #url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name = 'remove-course'),
    #Урлы для редактирования урока
#    url(r'^(?P<pk>\d+)/add_lesson/$', views.create_lesson, name = 'create-lesson'),
#    url(r'^(?P<pk>\d+)/edit_lesson/$', views.edit_lesson, name = 'edit-lesson'),
#    url(r'^(?P<pk>\d+)/remove_lesson/$', views.remove_lesson, name = 'remove-lesson'),
]

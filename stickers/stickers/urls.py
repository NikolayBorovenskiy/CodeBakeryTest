# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from stickers import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.show_index, name = 'index'),
    #url(r'^desktop/', include('tasks.urls', namespace = "tasks")),
    url(r'^accounts/', include('registration.urls')),
    url(r'^accounts/profile/', include('tasks.urls', namespace = "tasks")),
    url(r'', include('social_auth.urls')),
]

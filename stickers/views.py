# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import auth
from django.views.generic import TemplateView
from tasks.views import MixinUserContext


#Render Landing page (index.html)
class IndexView (MixinUserContext, TemplateView):
	template_name = 'index.html'
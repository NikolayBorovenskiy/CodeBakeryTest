# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import auth


#Render Landing page (index.html)
def show_index(request):
	cont = 1
    return render(request, 'index.html',
    	{'username': auth.get_user(request).username},)
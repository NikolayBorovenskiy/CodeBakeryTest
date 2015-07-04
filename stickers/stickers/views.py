# -*- coding: utf-8 -*-

from django.shortcuts import render


#Render Landing page (index.html)
def show_index(request):
    return render(request, 'index.html',)

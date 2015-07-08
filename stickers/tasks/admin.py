from django.contrib import admin
from django.contrib.auth.models import User

from tasks.models import Task, TaskItem



class TaskItemInLine(admin.TabularInline):
    model = TaskItem
    #field = ['theme', 'discription', 'number']
    item_display = ['discription', 'status']


class TaskAdmin(admin.ModelAdmin):
    search_fields = ['user', 'title']
    list_display = ['user', 'theme', 'title', 'time_public', 'impotent', 'fire']
    list_filter = ['user', 'impotent', 'theme', 'time_public', 'time_finish',]
    inlines = [TaskItemInLine]
    list_per_page = 20

class TaskItemAdmin(admin.ModelAdmin):
    list_display = ['commontask', 'discription', 'status']
    search_fields = ['commontask', 'discription']
    list_filter = ['status']



admin.site.register(Task, TaskAdmin)
admin.site.register(TaskItem, TaskItemAdmin)
#admin.site.register(User, UserAdmin)


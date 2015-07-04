from django.contrib import admin

from tasks.models import Task, TaskItem


class TaskItemInLine(admin.TabularInline):
    model = TaskItem
    #field = ['theme', 'discription', 'number']
    item_display = ['discription', 'status']

class TaskAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ['title', 'theme']
    inlines = [TaskItemInLine]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskItem)

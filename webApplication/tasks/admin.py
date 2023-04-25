from django.contrib import admin
from .models import TaskPriority, TaskType, TaskNote, Task

# Register your models here.
@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TaskNote)
class TaskNoteAdmin(admin.ModelAdmin):
    list_display = ['task','action', 'created']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'priority', 'type', 'description', 'completed']
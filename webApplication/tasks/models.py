from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class TaskPriority(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class TaskType(models.Model):
    name = models.CharField(TaskPriority, max_length=30, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.ForeignKey(TaskPriority, on_delete=models.CASCADE)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)


class TaskNote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)


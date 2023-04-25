from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Task, TaskNote

# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        tasks = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(tasks, self.paginate_by)

        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)
        context['tasks'] = tasks
        return context

class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    fields = ('title', 'priority', 'type', 'description')
    success_url = reverse_lazy('tasks-list')
    success_message = "Task was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'tasks'

    def get_context_data(self, *args, **kwargs):
        if self.request.GET.get('take-task') == 'yes':
            task = Task.objects.get(id=self.object.id)
            task.author = self.request.user
            task.completed = False
            task.save()
        context =  super().get_context_data(*args, **kwargs)
        context['notes'] = TaskNote.objects.filter(task__id=self.object.id)
        return context


class TaskNoteCreateView(LoginRequiredMixin, CreateView):
    model = TaskNote
    template_name = 'note/create.html'
    fields = ('action',)

    def get_success_url(self, **kwargs):
        return reverse_lazy('tasks-detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.task = get_object_or_404(Task, id=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        task = Task.objects.get(id=form.instance.task.id)
        task.completed = True
        task.save()
        return super().form_valid(form)
    

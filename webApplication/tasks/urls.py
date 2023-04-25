from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(),
        name='tasks-list'),
    path('create', views.TaskCreateView.as_view(),
        name='tasks-create'),
     path('<int:pk>/detail', views.TaskDetailView.as_view(),
        name='tasks-detail'),
    
    path('note/<int:pk>/create', views.TaskNoteCreateView.as_view(),
        name='task-note-create'),
]
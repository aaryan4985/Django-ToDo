from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('complete/<int:task_id>/', views.complete_task, name='complete-task'),
]

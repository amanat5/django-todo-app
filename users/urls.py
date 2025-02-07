from django.urls import path
from django.shortcuts import redirect
from .views import register, user_login, user_logout
from . import views
from .views import task_list

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login),  
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tasks/', task_list, name='task_list'),  
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/new/', views.create_task, name='create_task'),
    path('task/<int:task_id>/edit/', views.update_task, name='update_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]

from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/create', views.create_todo, name='create_todo'),
    path('todo/complete/<int:todo_id', views.complete_todo, name='complete_todo'),
    
]

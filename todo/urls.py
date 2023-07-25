from django.urls import path
from . import views

urlpatterns = [
    #addtask
    path('addtask/',views.add_task,name='add_task'),
    #mark_as done__task
    path('complete_task/<int:pk>/',views.complete_task,name='complete_task'),
    #mark_as undone__task
    path('uncomplete_task/<int:pk>/',views.uncomplete_task,name='uncomplete_task'),
    #edit_task
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    #delete_task
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task')
]
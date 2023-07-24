from django.urls import path
from . import views

urlpatterns = [
    #addtask
    path('addtask/',views.add_task,name='add_task'),
    #completed_task
    path('complete_task/<int:pk>',views.complete_task,name='complete_task')
]
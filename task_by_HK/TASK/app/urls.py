from django.urls import path
from .views import *

urlpatterns = [
    path('',add_User,name='add_User'),
    path('add_Task/',add_Task,name='add_Task'),
    path('user_list/',user_list,name='user_list'),
    path('task_list/',task_list,name='task_list'),
    path('export_excel_userData/',export_excel_userData,name='export_excel_userData'),
    path('export_excel_taskData/',export_excel_taskData,name='export_excel_taskData'),
]

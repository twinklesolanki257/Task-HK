from django.shortcuts import render,redirect
from .forms import *

from django.core.paginator import Paginator
import pandas

# Create your views here.

def add_User(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request,'add_user.html',{'form':form})


def add_Task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form})


def user_list(request):
    user = User.objects.all()
    paginator = Paginator(user,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'user_list.html',{'page_obj':page_obj})
    
def task_list(request):
    user = Task.objects.all()
    paginator = Paginator(user,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'task_list.html',{'page_obj':page_obj})
    

def export_excel_userData(request):
    user_objs = User.objects.all()
    user_data = []
    for obj in user_objs:
        user_data.append({
            'id' : obj.id,
            'name' : obj.name,
            'email' : obj.email,
            'mob' : obj.mob
        })
    pandas.DataFrame(user_data).to_excel('UserData.xlsx')
    return redirect('user_list')

def export_excel_taskData(request):
    task_objs = Task.objects.all()
    task_data = []
    for obj in task_objs:
        task_data.append({
            'id' : obj.id,
            'user_detail' : obj.user_detail,
            'task_detail' : obj.task_detail,
            'task_type' : obj.task_type
        })

    pandas.DataFrame(task_data).to_excel('TaskData.xlsx')
    return redirect('task_list')

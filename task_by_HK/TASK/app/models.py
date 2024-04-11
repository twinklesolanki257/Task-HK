from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mob = models.CharField(max_length=50)

class Task(models.Model):
    PENDING = "Pending"
    DONE = "Done"

    Task_Type = [
        (PENDING, "Pending"),
        (DONE,"Done")
    ]
    
    user_detail = models.ForeignKey(User, on_delete = models.CASCADE)
    task_detail = models.TextField()
    task_type = models.CharField(max_length=10, choices= Task_Type)
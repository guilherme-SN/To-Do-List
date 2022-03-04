from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=200) # name of the To Do List

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # ForeignKey used to create a relational database
    txt = models.CharField(max_length=300) # text field of each task
    checkComplete = models.BooleanField() # to check if we complete the task or not

    def __str__(self):
        return self.txt
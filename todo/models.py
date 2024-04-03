from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    # description = models.TextField()
    # completed = models.BooleanField(default=False)
    # created_at = models.DateField(auto_now=True)
     

    def __str__(self):
        return self.todo_name
    



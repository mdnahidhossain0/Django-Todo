from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=50)
    describtion= models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

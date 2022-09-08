from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['completed']

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time
#from DateTimeField import DateTimeField
# Create your models here.


class Task(models.Model):
    priority_choices = [
        ('1', '1️⃣'),
        ('2', '2️⃣'), 
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10','🔟'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True , null=True, blank=True)
    priority = models.CharField(max_length=2, choices=priority_choices, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
    

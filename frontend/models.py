from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    question = models.CharField(max_length=250, null=True)
    query_text = models.CharField(max_length=600, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=600, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer
    
class Graph(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    question = models.CharField(max_length=250, null=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    chart_data = models.JSONField(default=dict, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Chat(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    question = models.CharField(max_length=250, null=True)
    query_text = models.CharField(max_length=600, blank=True)
    answer = models.CharField(max_length=600, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
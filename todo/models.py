from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    posted_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    due_at= models.DateTimeField(null=True, blank=True)
    
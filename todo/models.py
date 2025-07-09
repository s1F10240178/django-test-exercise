from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    posted_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    due_at= models.DateTimeField(null=True, blank=True)
    
    def is_overdue(self, now=None):
        
        if self.due_at is None:
            return False
        if now is None:
            now = timezone.now()
        return self.due_at < now

from django.test import TestCase
from django.utils import timezone
from todo.models import Task
from datetime import datetime


# Create your tests here.

class TaskModelTestCase(TestCase):
    def test_task_creation(self):
      due= timezone.make_aware(datetime(2024,6,30,23,59,59))
      task=Task(title='task1',due_at=due)
      task.save()
      task=Task.objects.get(pk=task.pk)
      self.assertEqual(task.title, 'task1')
      self.assertEqual(task.due_at, due)
      self.assertFalse(task.completed)
   
    def test_create_task2(self):
        task = Task(title='task2')
        task.save()
        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'task2')
        self.assertIsNone(task.due_at,None)
        self.assertFalse(task.completed)
 
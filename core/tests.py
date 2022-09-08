from django.test import TestCase
from core.models import Task
# Create your tests here.
class TestTask(TestCase):
    def test_task(self):
        task = Task.objects.create(title="test",description="test",completed=True)
        self.assertEqual(str(task),'test')

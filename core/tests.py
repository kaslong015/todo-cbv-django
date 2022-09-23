from django.test import TestCase
from core.models import Task
from django.contrib.auth.models import User
# Create your tests here.
class TestTask(TestCase):
    def test_task(self):
        ''' create user instane called task_user and pass it as user ''''
        task_user = User.objects.create(username="test",password="test123@gh")
        task = Task.objects.create(user=task_user,title="test",description="test",completed=True)
        self.assertEqual(str(task),'test')

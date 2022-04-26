from django.db import models


class Task(models.Model):
    taskdetail = models.TextField()
    creator = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']



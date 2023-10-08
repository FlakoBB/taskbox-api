from django.db import models
from users.models import User

class Task(models.Model):
  PRIORITY_CHOICES = [
    ('Normal', 'Normal'),
    ('Urgente', 'Urgente')
  ]

  title = models.CharField(
    max_length=50,
    blank=False,
    null=False
  )
  description = models.TextField(
    blank=True
  )
  priority = models.CharField(
    max_length=10,
    choices=PRIORITY_CHOICES,
    default='Normal'
  )
  is_completed = models.BooleanField(
    default=False
  )
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user_id} - {self.title}'
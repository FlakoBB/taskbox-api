from django.db import models

class User(models.Model):
  username = models.CharField(
    max_length=30,
    unique=True,
    primary_key=True,
    blank=False,
    null=False
  )
  name = models.CharField(
    max_length=60,
    blank=False
  )
  surname = models.CharField(
    max_length=60,
    blank=True
  )
  password = models.CharField(
    max_length=100,
    blank=False,
    null=False
  )

  def __str__(self):
    return self.username
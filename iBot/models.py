from django.db import models

# Create your models here.
class chat(models.Model):
  request=models.CharField(max_length=400)
  response=models.CharField(max_length=400)

def __str__(self):
    return self.response    
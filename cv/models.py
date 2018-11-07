from django.db import models


# Create your models here.
class Penalty(models.Model):
    penalty = models.IntegerField(default=0)

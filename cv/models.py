from django.db import models


# Create your models here.
class Penalty(models.Model):
    name = models.TextField(default='user')
    penalty = models.IntegerField(default=0)
    diet_strike = models.IntegerField(default=0)
    non_smoking_strike = models.IntegerField(default=0)


from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Schedule(models.Model):
    day_date = models.DateField()
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    duration = models.DurationField()
    description = models.TextField()
    user = ForeignKey(User, on_delete=models.CASCADE, null=True)

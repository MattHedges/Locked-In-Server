from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):

    currentWeight = models.IntegerField()
    goalWeight = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timeframe = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
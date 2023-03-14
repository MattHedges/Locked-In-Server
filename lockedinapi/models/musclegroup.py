from django.db import models
from django.contrib.auth.models import User


class MuscleGroup(models.Model):

    muscle = models.CharField(max_length=50)

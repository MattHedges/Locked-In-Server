from django.db import models
from django.contrib.auth.models import User


class Routine(models.Model):

    name = models.CharField(max_length=50)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    exerciseRoutine = models.ManyToManyField("exercise", through="ExerciseRoutine" )
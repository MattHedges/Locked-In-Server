from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=1000, null=False)
    difficulty = models.ForeignKey("Difficulty", on_delete=models.CASCADE)
    muscleGroup = models.ForeignKey("MuscleGroup", on_delete=models.CASCADE)
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE)
    video = models.CharField(max_length=200, null=True)
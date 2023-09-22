from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    first_name = models.OneToOneField(User,max_length=50, null=False related_name="first_name")
    last_name = models.CharField(max_length=1000, null=False)
    description2 = models.CharField(max_length=1000, null=False)
    description3 = models.CharField(max_length=1000, null=True)
    description4 = models.CharField(max_length=1000, null=True)
    difficulty = models.ForeignKey("Difficulty", on_delete=models.CASCADE)
    muscleGroup = models.ForeignKey("MuscleGroup", on_delete=models.CASCADE)
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE)
    video = models.CharField(max_length=200, null=True)
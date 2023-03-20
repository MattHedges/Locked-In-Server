from django.db import models
from django.contrib.auth.models import User


class ExerciseRoutine(models.Model):

    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    routine = models.ForeignKey("Routine", on_delete=models.CASCADE, related_name = 'exercise_routine')

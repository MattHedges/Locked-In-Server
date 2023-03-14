from django.db import models
from django.contrib.auth.models import User


class Difficulty(models.Model):

    description = models.CharField(max_length=50)
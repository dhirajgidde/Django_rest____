from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

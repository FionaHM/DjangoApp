# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Snippets(models.Model):
    title = models.CharField(max_length=200, unique=True)
    language = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    snippet = models.TextField(blank=False)
    created_at = models.DateField(default=datetime.datetime.now, blank=True)
    updated_at = models.DateField(default=datetime.datetime.now, blank=True)

   
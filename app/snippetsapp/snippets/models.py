# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Snippets(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False)
    snippet = models.TextField(max_length=200, blank=False)
    created_at = models.DateField(default=datetime.datetime.now, blank=True)

  
   
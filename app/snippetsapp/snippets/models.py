# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Snippets(models.Model):
    # snippetid = models.AutoField(primary_key=True, blank=False,unique=True)
    title = models.CharField(max_length=100, blank=False)
    language = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False)
    snippet = models.CharField(max_length=300, blank=False)
    created_at = models.DateField(default=datetime.datetime.now, blank=True)
    updated_at = models.DateField(default=datetime.datetime.now, blank=True)

   
from django.db import models
from datetime import datetime

# Create your models here.
class biomodel(models.Model):
    bmKey = models.CharField(max_length=10, blank=False, primary_key=True)
    name =  models.CharField(max_length=100, blank=False)
    privacy = models.IntegerField(default=0, blank=False)
    ownerName = models.CharField(max_length=10, blank=True)
    saveDate = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name


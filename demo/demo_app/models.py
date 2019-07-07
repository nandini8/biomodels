from django.db import models

# Create your models here.
class biomodel(models.Model):
    bmKey = models.CharField(max_length=10, blank=False)
    name =  models.CharField(max_length=100, blank=False)
    privacy = models.IntegerField(default=0, blank=False)
    def __str__(self):
        return self.name


from django.db import models

class AppTwoModel(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)

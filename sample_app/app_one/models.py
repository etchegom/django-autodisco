from django.db import models

class AppOneModel(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)

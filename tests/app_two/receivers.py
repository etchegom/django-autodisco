from __future__ import annotations

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AppTwoModel


@receiver(post_save, sender=AppTwoModel)
def post_save_receiver(sender, instance, created, **kwargs):
    print("Hey! post_save signal of model AppTwoModel is connected!")

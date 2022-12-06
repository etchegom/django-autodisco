from django.dispatch import receiver


from django.db.models.signals import post_save
from .models import AppOneModel


@receiver(post_save, sender=AppOneModel)
def post_save_receiver(sender, instance, created, **kwargs):
    print("Hey! post_save signal of model AppOneModel is connected!")

from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
from django.conf import settings


class AutodiscoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autodisco"

    def ready(self) -> None:
        for mod in settings.AUTODISCO_MODULES:
            autodiscover_modules(mod)

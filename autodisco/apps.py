from __future__ import annotations

from django.apps import AppConfig
from django.conf import settings
from django.utils.module_loading import autodiscover_modules


class AutodiscoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autodisco"

    def ready(self) -> None:
        for mod in settings.AUTODISCO_MODULES:
            autodiscover_modules(mod)

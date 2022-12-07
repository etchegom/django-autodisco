from __future__ import annotations

from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import autodiscover_modules


class AutodiscoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autodisco"

    def ready(self) -> None:
        if not isinstance(settings.AUTODISCO_MODULES, list):
            raise ImproperlyConfigured("AUTODISCO_MODULES must be a list")
        for mod in sorted(
            [str(m) for m in settings.AUTODISCO_MODULES if m not in ("models", "admin")]
        ):
            autodiscover_modules(mod)

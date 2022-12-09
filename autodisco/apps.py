from __future__ import annotations

from importlib import import_module

from django.apps import AppConfig, apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import module_has_submodule


def autodiscover_modules(app_config: AppConfig, modules: list[str]) -> None:
    for module_name in modules:
        try:
            import_module(name=f"{app_config.name}.{module_name}")
        except Exception:
            if module_has_submodule(
                package=app_config.module,
                module_name=module_name,
            ):
                raise


class AutodiscoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autodisco"

    def ready(self) -> None:
        autodisco_modules = getattr(settings, "AUTODISCO_MODULES", None)
        if autodisco_modules is None:
            raise ImproperlyConfigured("AUTODISCO_MODULES is missing")
        if not isinstance(autodisco_modules, list):
            raise ImproperlyConfigured("AUTODISCO_MODULES must be a list")

        autodisco_apps = getattr(settings, "AUTODISCO_APPS", None)
        if autodisco_apps and not isinstance(autodisco_apps, list):
            raise ImproperlyConfigured("AUTODISCO_APPS must be a list")

        modules = sorted(
            [str(m) for m in settings.AUTODISCO_MODULES if m not in ("models", "admin")]
        )

        for app_config in apps.get_app_configs():
            if app_config.name == "autodisco" or app_config.name.startswith("django.contrib"):
                continue
            if autodisco_apps and app_config.name not in autodisco_apps:
                continue
            autodiscover_modules(app_config=app_config, modules=modules)

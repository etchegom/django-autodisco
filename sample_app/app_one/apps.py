from __future__ import annotations

from django.apps import AppConfig


class AppOneConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_one"

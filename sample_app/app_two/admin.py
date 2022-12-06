from __future__ import annotations

from django.contrib import admin

from .models import AppTwoModel


@admin.register(AppTwoModel)
class AppTwoModelAdmin(admin.ModelAdmin):
    pass

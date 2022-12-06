from django.contrib import admin
from .models import AppOneModel


@admin.register(AppOneModel)
class AppOneModelAdmin(admin.ModelAdmin):
    pass

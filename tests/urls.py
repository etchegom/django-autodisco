from __future__ import annotations

from django.urls import path
from django.views import debug

urlpatterns = [
    path("", debug.default_urlconf),
]

from __future__ import annotations

from unittest.mock import call, patch

from django.apps import apps
from django.test import TestCase, override_settings


class AutodiscoConfigTest(TestCase):
    @override_settings(AUTODISCO_MODULES=["module_a", "module_b"])
    def test_apps(self):
        autodisco_app = apps.get_app_config("autodisco")
        with patch("autodisco.apps.autodiscover_modules") as mock_autodiscover:
            autodisco_app.ready()
            mock_autodiscover.assert_has_calls(
                calls=[
                    call("module_a"),
                    call("module_b"),
                ],
                any_order=True,
            )

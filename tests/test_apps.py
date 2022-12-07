from __future__ import annotations

from unittest.mock import call, patch

from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings


class AutodiscoConfigTest(TestCase):
    def _get_autodisco_app(self):
        return apps.get_app_config("autodisco")

    @override_settings(AUTODISCO_MODULES=["module_b", "module_a"])
    @patch("autodisco.apps.autodiscover_modules")
    def test_autodiscover_called_on_ready(self, mock_autodiscover):
        self._get_autodisco_app().ready()
        mock_autodiscover.assert_has_calls(
            calls=[
                call("module_a"),
                call("module_b"),
            ],
        )

    @override_settings(AUTODISCO_MODULES=True)
    @patch("autodisco.apps.autodiscover_modules")
    def test_improperly_configured(self, mock_autodiscover):
        autodisco_app = self._get_autodisco_app()
        with self.assertRaises(ImproperlyConfigured):
            autodisco_app.ready()
        mock_autodiscover.assert_not_called()

    @override_settings(AUTODISCO_MODULES=[123456])
    @patch("autodisco.apps.autodiscover_modules")
    def test_non_str_module_name(self, mock_autodiscover):
        self._get_autodisco_app().ready()
        mock_autodiscover.assert_called_once_with("123456")

    @override_settings(AUTODISCO_MODULES=["module", "models", "admin"])
    @patch("autodisco.apps.autodiscover_modules")
    def test_ignore_reserved_module_names(self, mock_autodiscover):
        self._get_autodisco_app().ready()
        mock_autodiscover.assert_called_once_with("module")

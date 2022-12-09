from __future__ import annotations

from unittest.mock import call, patch

from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings


@patch("autodisco.apps.import_module")
class AutodiscoConfigTest(TestCase):
    def _get_autodisco_app(self):
        return apps.get_app_config("autodisco")

    @override_settings(AUTODISCO_MODULES=None)
    def test_autodisco_modules_is_missing(self, mock_import_module):
        autodisco_app = self._get_autodisco_app()
        with self.assertRaises(ImproperlyConfigured) as exc:
            autodisco_app.ready()
            assert str(exc) == "AUTODISCO_MODULES is missing"
        mock_import_module.assert_not_called()

    @override_settings(AUTODISCO_MODULES=True)
    def test_autodisco_modules_is_not_a_list(self, mock_import_module):
        autodisco_app = self._get_autodisco_app()
        with self.assertRaises(ImproperlyConfigured) as exc:
            autodisco_app.ready()
            assert str(exc) == "AUTODISCO_MODULES must be a list"
        mock_import_module.assert_not_called()

    @override_settings(AUTODISCO_APPS=True)
    def test_autodisco_apps_is_not_a_list(self, mock_import_module):
        autodisco_app = self._get_autodisco_app()
        with self.assertRaises(ImproperlyConfigured) as exc:
            autodisco_app.ready()
            assert str(exc) == "AUTODISCO_APPS must be a list"
        mock_import_module.assert_not_called()

    @override_settings(AUTODISCO_MODULES=["module_b", "module_a"])
    def test_import_modules(self, mock_import_module):
        self._get_autodisco_app().ready()
        mock_import_module.assert_has_calls(
            calls=[
                call(name="app_one.module_a"),
                call(name="app_one.module_b"),
                call(name="app_two.module_a"),
                call(name="app_two.module_b"),
            ],
        )

    @override_settings(
        AUTODISCO_MODULES=["module_b", "module_a"],
        AUTODISCO_APPS=["app_one"],
    )
    def test_import_modules_with_app_filter(self, mock_import_module):
        self._get_autodisco_app().ready()
        mock_import_module.assert_has_calls(
            calls=[
                call(name="app_one.module_a"),
                call(name="app_one.module_b"),
            ],
        )

    @override_settings(AUTODISCO_MODULES=[123456])
    def test_non_str_module_name(self, mock_import_module):
        self._get_autodisco_app().ready()
        mock_import_module.assert_has_calls(
            calls=[
                call(name="app_one.123456"),
                call(name="app_two.123456"),
            ]
        )

    @override_settings(AUTODISCO_MODULES=["models", "admin"])
    def test_ignore_reserved_module_names(self, mock_import_module):
        self._get_autodisco_app().ready()
        mock_import_module.assert_not_called()

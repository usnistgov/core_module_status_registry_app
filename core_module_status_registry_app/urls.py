""" Url router for the Status registry module
"""

from django.urls import re_path

from core_module_status_registry_app.views.views import StatusRegistryModule

urlpatterns = [
    re_path(
        r"module-status-registry",
        StatusRegistryModule.as_view(),
        name="core_module_status_registry_view",
    ),
]

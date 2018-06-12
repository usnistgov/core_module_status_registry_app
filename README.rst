core_module_status_registry_app
===============================

Status registry module

Quick start
===========

1. Add "core_module_status_registry_app" to your INSTALLED_APPS setting
-----------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_module_status_registry_app',
    ]

2. Include the core_module_status_registry_app URLconf in your project urls.py
------------------------------------------------------------------------------

.. code:: python

    url(r'^', include('core_module_status_registry_app.urls')),
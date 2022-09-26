""" Status registry Module
"""
from core_main_registry_app.commons.constants import DataStatus
from core_parser_app.tools.modules.views.builtin.options_module import (
    AbstractOptionsModule,
)


class StatusRegistryModule(AbstractOptionsModule):
    """Status Registry Module"""

    def __init__(self):
        self.options = {
            DataStatus.INACTIVE: "Inactive",
            DataStatus.ACTIVE: "Active",
        }

        AbstractOptionsModule.__init__(
            self, options=self.options, disabled=False
        )

    def _retrieve_data(self, request):
        """Retrieve module's data

        Args:
            request:

        Returns:

        """
        # default value is active
        data = DataStatus.ACTIVE
        self.selected = data
        # GET module data
        if request.method == "GET":
            if "data" in request.GET:
                data = request.GET["data"]
                # Add deleted option only if editing a data with deleted status
                if (
                    data == DataStatus.DELETED
                    and DataStatus.DELETED not in self.options
                ):
                    self.options[DataStatus.DELETED] = "Deleted"
                self.selected = data
        # POST module data
        elif request.method == "POST":
            if "data" in request.POST:
                data = request.POST["data"]
        return data

    def _render_data(self, request):
        """Return module's data rendering

        Args:
            request:

        Returns:

        """
        return ""

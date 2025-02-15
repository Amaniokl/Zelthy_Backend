from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol
from .models import Issue
from .forms import IssueForm, DeleteIssueForm


class IssueTable(ModelTable):
    id = ModelCol(display_as="ID", sortable=True, searchable=True)
    title = ModelCol(display_as="Title", sortable=True, searchable=True)
    description = ModelCol(display_as="Description", sortable=True, searchable=True)
    status = ModelCol(display_as="Status", sortable=True)
    assignee = ModelCol(display_as="Assigned By", sortable=True, searchable=True)

    table_actions = []
    row_actions = [
        {
            "name": "Edit Issue",
            "key": "edit_issue",
            "description": "Edit Issue record",
            "type": "form",
            "form": IssueForm,
        },
        {
            "name": "Delete Issue",
            "key": "delete_issue",
            "description": "Delete Issue record",
            "type": "form",
            "form": DeleteIssueForm,
        },
    ]

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "assignee"]
        row_selector = {"enabled": False, "multi": False}

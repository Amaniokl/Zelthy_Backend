from ..packages.crud.forms import BaseForm
from ..packages.crud.forms import BaseSimpleForm
from ..packages.crud.form_fields import ModelField
from .models import Issue
from django import forms


class IssueForm(BaseForm):
    title = ModelField(
        placeholder="Enter Title",
        required=True,
        required_msg="This field is required.",
    )
    description = ModelField(
        placeholder="Enter Description",
        required=True,
        required_msg="This field is required.",
    )
    assignee = ModelField(
        placeholder="Select Assignee",
        required=True,
        required_msg="This field is required.",
    )

    class Meta:
        title = "Issues"
        model = Issue


class DeleteIssueForm(BaseSimpleForm):
    reason = forms.CharField(label="Reason", max_length=100, required=True)

    class Meta:
        title = "Delete Issue"
        model = Issue

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)

    def save(self):
        try:
            if self.instance:
                self.instance.delete()
        except Exception as e:
            print(f"Error deleting issue: {e}")

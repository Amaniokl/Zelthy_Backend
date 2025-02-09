from zango.models import ZModel, ZForeignKey, ZCharField, ZTextField, ZEnumField, ZTimestampField
from zango.auth.models import AppUserModel

class IssueModel(ZModel):
    title = ZCharField(max_length=255)
    description = ZTextField()
    status = ZEnumField(choices=["Open", "In Progress", "Resolved"], default="Open")
    assignee = ZForeignKey(to=AppUserModel, related_name="assigned_issues", null=True)
    created_at = ZTimestampField(auto_now_add=True)
    updated_at = ZTimestampField(auto_now=True)

    class Meta:
        table_name = "issues"

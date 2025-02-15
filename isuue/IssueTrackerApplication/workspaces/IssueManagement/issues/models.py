from zango.apps.dynamic_models.models import DynamicModelBase
from django.db import models
from zango.apps.dynamic_models.fields import ZForeignKey
from zango.apps.appauth.models import AppUserModel


class Issue(DynamicModelBase):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"

    ISSUE_STATUS_CHOICES = [
        (OPEN, "Open"),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, "Resolved"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=ISSUE_STATUS_CHOICES, default=OPEN
    )
    assignee = ZForeignKey(
        AppUserModel, on_delete=models.SET_NULL, null=True, blank=True
    )

    # created_at and updated_at are inherited from DynamicModelBase

    def __str__(self):
        return f"{self.id} {self.title} {self.status}"

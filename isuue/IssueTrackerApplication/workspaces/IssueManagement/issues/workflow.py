from ..packages.workflow.base.engine import WorkflowBase
from .models import Issue
from ..packages.communication.email.utils import Email
from zango.apps.appauth.models import AppUserModel


class IssueWorkflow(WorkflowBase):
    status_transitions = [
        {
            "name": "start_progress",
            "display_name": "Start Progress",
            "description": "Move issue from Open to In Progress",
            "confirmation_message": "Are you sure you want to start working on this issue?",
            "from": "open",
            "to": "in_progress"
        },
        {
            "name": "resolve",
            "display_name": "Resolve Issue",
            "description": "Mark issue as resolved",
            "confirmation_message": "Are you sure you want to resolve this issue?",
            "from": "in_progress",
            "to": "resolved"
        },
        {
            "name": "reopen",
            "display_name": "Reopen Issue",
            "description": "Move issue back to Open",
            "confirmation_message": "Are you sure you want to reopen this issue?",
            "from": "resolved",
            "to": "open"
        }
    ]

    ### Transition Conditions ###
    def start_progess_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "open"

    def resolved_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "in_progress"

    def reopen_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "resolved"

    ### Processing Methods ###
    def start_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = "in_progress"
        # if object_instance.assignee:
        #     assignee_email = object_instance.assignee.email
        #     self.send_email_to_assignee(assignee_email)
        object_instance.save()

    def resolve_done(self, request, object_instance, transaction_obj):
        object_instance.status = "resolved"
        # print("resolved")
        # if object_instance.assignee:
        #     print("Hai")
        #     assignee_email = object_instance.assignee.email
        #     self.send_email_to_assignee(assignee_email)
        object_instance.save()

    def reopen_done(self, request, object_instance, transaction_obj):
        object_instance.status = "open"
        object_instance.save()

    # def send_email_to_assignee(self, to_email):
    #     print("sending email....")
    #     email = Email(
    #         to=to_email,  # Recipient email address
    #         subject='Your Issue Updated',  # Email subject
    #         body='The status of your issue updated'  # Email body content
    #     )
    #     email.send_email()
    #     print('email sent')

    class Meta:
        model = Issue
        statuses = {
            "open": {
                "color": "#FF4C4C",
                "label": "Open"
            },
            "in_progress": {
                "color": "#FFC107",
                "label": "In Progress"
            },
            "resolved": {
                "color": "#4CAF50",
                "label": "Resolved"
            }
        }
        on_create_status = "open"

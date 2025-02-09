from zango.http import ZRequest, ZResponse
from zango.shortcuts import get_object_or_404
from zango.decorators import login_required
from .models import IssueModel

@login_required
def create_issue(request: ZRequest):
    data = request.json
    issue = IssueModel.create(
        title=data["title"],
        description=data["description"],
        status=data.get("status", "Open"),
        assignee=data.get("assignee")
    )
    return ZResponse.json(issue.to_dict(), status=201)

@login_required
def list_issues(request: ZRequest):
    status = request.query.get("status")
    assignee = request.query.get("assignee")
    query = IssueModel.query

    if status:
        query = query.filter(IssueModel.status == status)
    if assignee:
        query = query.filter(IssueModel.assignee == assignee)

    issues = query.all()
    return ZResponse.json([issue.to_dict() for issue in issues])

@login_required
def update_issue(request: ZRequest, issue_id):
    issue = get_object_or_404(IssueModel, id=issue_id)
    data = request.json

    if "title" in data:
        issue.title = data["title"]
    if "description" in data:
        issue.description = data["description"]
    if "status" in data:
        issue.status = data["status"]
    if "assignee" in data:
        issue.assignee = data["assignee"]

    issue.save()
    return ZResponse.json(issue.to_dict())

@login_required
def delete_issue(request: ZRequest, issue_id):
    issue = get_object_or_404(IssueModel, id=issue_id)
    issue.delete()
    return ZResponse.json({"message": "Issue deleted successfully."})

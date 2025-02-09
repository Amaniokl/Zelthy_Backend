from zango.routing import ZRouter
from .views import create_issue, list_issues, update_issue, delete_issue

router = ZRouter()

router.post("/issues", create_issue)
router.get("/issues", list_issues)
router.put("/issues/<int:issue_id>", update_issue)
router.delete("/issues/<int:issue_id>", delete_issue)

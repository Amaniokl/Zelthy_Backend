from zango import ZApp
from zango.auth import auth_router
from .urls import router
from .models import IssueModel
import zango
print(dir(zango))
app = ZApp()

# Register the authentication and main routes
app.include_router(auth_router)
app.include_router(router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

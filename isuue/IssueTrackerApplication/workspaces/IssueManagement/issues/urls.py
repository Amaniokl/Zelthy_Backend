from django.urls import path
from .views import IssueCrudView

urlpatterns = [
    path('all/', IssueCrudView.as_view(), name='issue_crud'),
]

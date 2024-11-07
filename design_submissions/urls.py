from django.urls import path
from . import views

urlpatterns = [
    path("submit-design/", views.submit_design, name="submit_design"),
    path(
        "delete-submission/<int:submission_id>/",
        views.delete_submission,
        name="delete_submission",
    ),
]

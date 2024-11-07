from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>",
        views.order_history,
        name="order_history"
        ),
    path(
        "order_detail/<order_number>/",
        views.order_detail,
        name="order_detail"
        ),
    path(
        "submit_review/<int:product_id>/",
        views.submit_review,
        name="submit_review"
        ),
]

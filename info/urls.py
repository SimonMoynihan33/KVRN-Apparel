from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="about"),
    path(
        "admin/messages/",
        views.contact_messages_view,
        name="contact_messages"
        ),
    path("faq/", views.faq_page, name="faq"),
]

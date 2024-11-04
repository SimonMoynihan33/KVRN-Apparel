from django.urls import path
from . import views

urlpatterns = [
    path('submit-design/', views.submit_design, name='submit_design'),
    path(
        'delete-submission/<int:submission_id>/',
        views.delete_submission, name='delete_submission'),
    path('edit-submission/<int:submission_id>/',
         views.edit_submission, name='edit_submission'),
]

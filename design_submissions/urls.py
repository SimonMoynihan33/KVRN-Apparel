from django.urls import path
from . import views

urlpatterns = [
    path('submit-design/', views.submit_design, name='submit_design'),
]

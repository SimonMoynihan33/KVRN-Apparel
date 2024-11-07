from django.db import models
from django.contrib.auth.models import User


class UserDesignSubmission(models.Model):
    """
    Model to allow user submissions of designs
    for graphic mockups
    """

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("processing", "Processing"),
        ("finalized", "Finalized"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="design_submissions/")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="submitted"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

from django.db import models
from django.conf import settings
from products.models import Product


class Wishlist(models.Model):
    """
    Model representing a user's wishlist item.

    Each wishlist entry links a user to a specific product, with the
    date the item was added. Ensures unique product entries per user
    through a unique constraint.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.product.name}"

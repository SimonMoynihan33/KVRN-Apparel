from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    """
    Category model to render 
    Boutique Ado Model 
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('men', 'Men'), ('women', 'Women')], null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ 
    Product model for displaying each product and information
    Boutique Ado Model 
    """
    GENDER_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women')
    ]
    categories = models.ManyToManyField('Category', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = MarkdownxField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

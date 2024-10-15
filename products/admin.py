from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register and extend admin panel for Categories
    """
    list_display = ('friendly_name', 'name', 'gender')  # Add gender to the list display
    list_filter = ('gender',)


# Customize the Product admin interface
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Register and extend admin panel for Products
    """
    list_display = (
        'sku',
        'name',
        'get_categories', # Method to display categories
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)
    list_filter = ('categories',)
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',)

    def get_categories(self, obj):
        """
        Returns a comma-separated list of category names for a product in the admin interface.
        Used in the ProductAdmin list_display to handle the Many-to-Many relationship for categories.
        """
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories' 

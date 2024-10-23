from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register and extend admin panel for Categories
    """
    list_display = ('friendly_name', 'name', 'gender')
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
        'get_categories',  # Method to display categories
        'price',
        'rating',
        'image_tag',
        'image2_tag',
    )
    ordering = ('sku',)
    list_filter = ('categories',)
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',)

    def get_categories(self, obj):
        """
        Returns a comma-separated list of category names for a product in the
        admin interface. Used in the ProductAdmin list_display to handle the
        Many-to-Many relationship for categories.
        """
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

    def image_tag(self, obj):
        """
        Returns an HTML image tag for the main product image.
        Displayed in the admin list_display as a small thumbnail.
        Created with AI.
        """
        if obj.image:  # Check if there is a main image
            return format_html(
                '<img src="{}" style="height:50px;"/>'.format(obj.image.url))
        return "No Image"  # Fallback if no image is available
    image_tag.short_description = 'Image'  # Set column name in admin

    def image2_tag(self, obj):
        """
        Returns an HTML image tag for the second product image.
        Displayed in the admin list_display as a small thumbnail.
        Created with AI.
        """
        if obj.image2:  # Check if there is a second image
            return format_html(
                '<img src="{}" style="height:50px;"/>'.format(obj.image2.url))
        return "No Image"  # Fallback if no second image is available
    image2_tag.short_description = 'Image 2'  # Set column name in admin

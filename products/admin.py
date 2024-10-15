from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name', 'gender')  # Add gender to the list display
    list_filter = ('gender',)

# Customize the Product admin interface
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories' 

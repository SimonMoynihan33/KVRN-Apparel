from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name', 'gender')  # Add gender to the list display
    list_filter = ('gender',)

# Customize the Product admin interface
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating')
    list_filter = ('categories',)
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',)

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class StaticViewSitemap(Sitemap):
    """
    Sitemap for static views that rarely change, such as home, about, etc.
    Priority is set relatively high as they are core pages, and frequency is
    set to yearly.
    """
    priority = 0.8
    changefreq = 'yearly'

    def items(self):
        """
        Returns a list of static view names to be included in the sitemap.
        Uses Django Allauth's URL names for signup and login.
        """
        return ['home', 'about', 'account_signup', 'account_login', 'view_bag',
                'faq']

    def location(self, item):
        """
        Resolves the URL for each item in the sitemap.
        """
        return reverse(item)


class ProductSitemap(Sitemap):
    """
    Sitemap for individual product pages.
    Priority is moderate as product pages are important, and frequency is set
    to weekly to account for potential updates or new product additions.
    """
    priority = 0.64
    changefreq = 'weekly'

    def items(self):
        """
        Returns a queryset of all products to be included in the sitemap.
        """
        return Product.objects.all()

    def lastmod(self, obj):
        """
        Returns the last modified date for each product, used for sitemap
        freshness.
        """
        return obj.updated_at


class ProductCategorySitemap(Sitemap):
    """
    Sitemap for product category pages, which may change occasionally.
    Priority is set high, and frequency is set to monthly.
    """
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        """
        Returns a list of category view names for the sitemap.
        """
        return []

    def location(self, item):
        """
        Resolves the URL for each category item in the sitemap.
        """
        return reverse(item)


class GeneralProductsSitemap(Sitemap):
    """
    Sitemap for the general products page, allowing users to access a filtered
    view of products. Priority is set relatively high since this page provides
    primary access to product listings.
    """
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        """
        Returns a list containing the general products view, which supports
        filtering by gender.
        """
        return ['products']

    def location(self, item):
        """
        Resolves the URL for the general products page.
        """
        return reverse(item)

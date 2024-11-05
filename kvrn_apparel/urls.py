"""
URL configuration for kvrn_apparel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    StaticViewSitemap,
    ProductSitemap,
    GeneralProductsSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'general_products': GeneralProductsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('profile/', include('profiles.urls')),
    path('about/', include('info.urls')),
    path('design_submissions/', include('design_submissions.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('privacy-policy/', TemplateView.as_view(
        template_name="privacy_policy.html"), name='privacy_policy'),
    path('cookie-policy/', TemplateView.as_view(
        template_name="cookie_policy.html"), name='cookie_policy'),
    path('terms-and-conditions/', TemplateView.as_view(
        template_name="terms_and_conditions.html"), name='terms_and_conditions'
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

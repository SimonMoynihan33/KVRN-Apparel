from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product


def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(
        request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)
    if created:
        pass
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')


@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)
    if created:
        # If the item was added to the wishlist
        messages.success(
            request, f"Added '{product.name}' to your wishlist.",
            extra_tags='wishlist')
    else:
        # If the item was already in the wishlist and is now being removed
        wishlist_item.delete()
        messages.success(
            request, f"Removed '{product.name}' from your wishlist.",
            extra_tags='wishlist')

    return redirect(request.META.get(
        'HTTP_REFERER', reverse('product_detail', args=[product.id])))

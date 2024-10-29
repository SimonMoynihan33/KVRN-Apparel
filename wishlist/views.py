from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    # Extract only the products from the wishlist items
    products = [item.product for item in wishlist_items]
    return render(
        request, 'wishlist/wishlist.html', {'products': products}
    )


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)
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
        # Item was added to the wishlist
        wishlist_state = True
    else:
        # Item was already in wishlist and is now removed
        wishlist_item.delete()
        wishlist_state = False

    # Return JSON response with the wishlist state
    return JsonResponse({
        'success': True,
        'wishlist_state': wishlist_state
    })

    # Return an error response for non-POST requests
    return JsonResponse(
        {'success': False, 'error': 'Invalid request'}, status=400)

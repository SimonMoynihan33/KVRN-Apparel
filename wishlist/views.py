from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


def wishlist_view(request):
    """
    Display the user's wishlist.

    Retrieves all wishlist items for the logged-in user and extracts
    the associated products. Renders the wishlist page with these products.
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    # Extract only the products from the wishlist items
    products = [item.product for item in wishlist_items]
    return render(
        request, 'wishlist/wishlist.html', {'products': products}
    )


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.

    Fetches the specified product by ID and creates a wishlist item
    if it doesn't already exist. Redirects to the wishlist page.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist.

    Fetches the specified product by ID and deletes the corresponding
    wishlist item if it exists. Redirects to the wishlist page.
    """
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')


def toggle_wishlist(request, product_id):
    """
    Toggle a product's presence in the user's wishlist.

    If the user is not logged in, redirects them to the login page with a
    message. If the user is logged in, toggles the product in the wishlist.
    """
    if not request.user.is_authenticated:
        # Add a message for the user and redirect to login if not authenticated
        messages.info(request, 'You must be logged in to add items to your \
            wishlist.')
        return JsonResponse({'redirect_url': reverse('account_login')})

    # User is authenticated; proceed with wishlist toggle
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

    # Return JSON response indicating the wishlist state
    return JsonResponse({
        'success': True,
        'wishlist_state': wishlist_state
    })

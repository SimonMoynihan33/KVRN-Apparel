from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm, ReviewForm
from checkout.models import Order, OrderReview
from products.models import Product


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)
    reviewed_products = OrderReview.objects.filter(
        user=request.user).values_list(
        "product_id", flat=True
    )

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
        "reviewed_products": reviewed_products,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display a past order confirmation.

    Retrieves the specified order by its order number and informs the user
    that this is a historical confirmation. The confirmation message is shown
    on the checkout success template with limited context.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


@login_required
def submit_review(request, product_id):
    """
    Handle the submission or update of a product review.

    Retrieves the relevant product and the latest order associated with
    the user's profile. If a review already exists, updates it; otherwise,
    creates a new review. On successful submission, redirects to the user's
    profile and displays a success message.
    """
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.filter(
        user_profile=request.user.userprofile, lineitems__product=product
    ).latest("date")
    existing_review = OrderReview.objects.filter(
        user=request.user, product=product
    ).first()
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.order = order
            review.save()
            if existing_review:
                messages.success(request, "Your review has been updated.")
            else:
                messages.success(
                    request, "Thank you! Your rating has been submitted.")
            return redirect("profile")
        else:
            messages.error(
                request,
                "There was an issue with your rating submission.\
                     Please try again.",
            )

    return redirect("profile")


@login_required
def order_detail(request, order_number):
    """
    Display detailed information for a specific order.

    Retrieve the order associated with the user and the specified order number.
    Checks if each product in the order has been reviewed by the user and
    annotates the line items accordingly. Renders the order detail template
    with the order and review status for each item.
    """
    # Retrieve the order associated with the user and the specific order number
    order = get_object_or_404(
        Order, order_number=order_number, user_profile=request.user.userprofile
    )
    # Fetch the rating for each product reviewed by the user
    reviewed_products = {
        review.product_id: review.rating
        for review in OrderReview.objects.filter(user=request.user)
    }
    for item in order.lineitems.all():
        item.is_reviewed = (
            item.product_id in reviewed_products if item.product else False
        )

    return render(
        request,
        "profiles/order_detail.html",
        {
            "order": order,
            "reviewed_products": reviewed_products,
        },
    )

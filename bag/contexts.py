from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    # For later use
    # user_country = request.user.profile.country if request.user.is_authenticated else None

    user_country = None

    if request.user.is_authenticated:
        pass

    # Free delivery for ROI (Republic of Ireland), 15% delivery charge for others
    if user_country == 'IE':
        delivery = 0  # Free delivery for ROI
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context

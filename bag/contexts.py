from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    quantity = 0
    bag = request.session.get('bag', {})

    # Calculate the total cost of items in the bag
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        # If the item is stored as an integer (just quantity), multiply it by the product's price
        if isinstance(item_data, int):
            subtotal = item_data * product.price  # Calculate subtotal per item
            total += subtotal  # Add to total
            bag_items.append({
                'item_id': item_id,
                'product': product,
                'quantity': item_data,
                'subtotal': subtotal,  # Store subtotal for template
            })
        # If the item is a dict (containing sizes and quantities), sum the quantities
        else:
            for size, quantity in item_data['items_by_size'].items():
                subtotal = quantity * product.price
                total += subtotal
                bag_items.append({
                    'item_id': item_id,
                    'product': product,
                    'size': size,
                    'quantity': quantity,
                    'subtotal': subtotal,  # Store subtotal for template
                })

    # Simplified delivery fee logic
    delivery = Decimal("0") if total >= Decimal("80") else Decimal("4.99")
    free_delivery_delta = 80 - total if total < 80 else 0

    grand_total = Decimal(total) + delivery  # Final total including delivery fee

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context

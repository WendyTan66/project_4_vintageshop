from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag = request.session.get('bag', {})  # Ensure bag is a dictionary
    # If 'bag' is None or not a dictionary, reset to an empty dictionary
    bag_items = []
    total = 0

    # Calculate the total cost of items in the bag
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=int(item_id))
        print(f"Retrieved product: {product.name}, Price: {product.price}")

        # No need for size logic anymore, treat all items as single instances
        subtotal = product.price  # No quantity or size
        total += subtotal
        
        bag_items.append({
            'item_id': item_id,
            'product': product,
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

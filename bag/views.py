from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    # Get the shopping bag from the session, or initialize it as an empty dictionary if not found
    bag = request.session.get('bag', {})

    # Prepare the list of bag items for rendering
    bag_items = []
    for item_id, quantity in bag.items():
        # Fetch product details from the Product model using item_id
        try:
            product = Product.objects.get(id=item_id)
            bag_items.append({
                'item_id': item_id,
                'product': product  # Now we append the full product details
            })
        except Product.DoesNotExist:
            continue  # Handle the case where the product is not found

    return render(request, 'bag/bag.html', {'bag_items': bag_items})

def add_to_bag(request, item_id):
    """ Add the specified product to the shopping bag """
    
    # Get the redirect URL from POST data (return user to the same page or elsewhere)
    redirect_url = request.POST.get('redirect_url', '/')

    # Get the shopping bag from the session, or initialize it as an empty dictionary if not found
    bag = request.session.get('bag', {})

    # Retrieve the product by ID
    product = get_object_or_404(Product, pk=item_id)
    
    # Add the product to the bag if it doesn't already exist
    if item_id not in bag:
        bag[item_id] = {
            'name': product.name,  # Access product's name field
            'price': str(product.price),  # Convert Decimal price to string for session storage
        }

    # Save the updated bag back to the session
    request.session['bag'] = bag

    # Redirect to the desired URL
    # In add_to_bag view
   
    print("Session bag contents:", request.session.get('bag'))
    return redirect(redirect_url)

from django.http import HttpResponse

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        # Get the shopping bag from the session
        bag = request.session.get('bag', {})

        # Remove the item from the bag
        if item_id in bag:
            del bag[item_id]  # Simply delete the item by item_id
        
        # Save the updated bag to the session
        request.session['bag'] = bag

        # Return a successful response
        return HttpResponse(status=200)
    
    except Exception as e:
        # In case of an error, return a server error response
        return HttpResponse(status=500)


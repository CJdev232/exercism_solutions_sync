"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item not in current_cart:
            current_cart[item]=1
        else:
            current_cart[item]+=1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    current_cart={}
    for item in notes:
        if item not in current_cart:
            current_cart[item]=1
        else:
            current_cart[item]+=1
    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for recipe_name,ingredients in recipe_updates:
        ideas[recipe_name]=ingredients
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    
    # Iterate through cart items only
    for item in cart:
        quantity = cart[item]
        aisle = aisle_mapping[item][0]
        refrigeration = aisle_mapping[item][1]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]
    
    # Sort in REVERSE alphabetical order
    return dict(sorted(fulfillment_cart.items(), reverse=True))
        
        


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, details in fulfillment_cart.items():
        quantity_ordered = details[0]
        quantity_available = store_inventory[item][0]
        aisle = store_inventory[item][1]
        refrigeration = store_inventory[item][2]
        
        # Calculate new quantity
        new_quantity = quantity_available - quantity_ordered
        
        # Check if out of stock (0 or less)
        if new_quantity <= 0:
            store_inventory[item] = ['Out of Stock', aisle, refrigeration]
        else:
            store_inventory[item] = [new_quantity, aisle, refrigeration]
    
    return store_inventory
            

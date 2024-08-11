from shopping_cart import ShoppingCart

def test_can_add_item_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    assert cart.size() == 1

# def test_item_added_cart_contain_items():

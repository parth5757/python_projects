from shopping_cart import ShoppingCart
import pytest



def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1

# def test_item_added_cart_contain_items():

def test_when_item_added_cart_contain_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()



def test_when_more_than_max_item_than_failed():
    cart = ShoppingCart(5)
    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add("apple")
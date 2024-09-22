from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

# def test_item_added_cart_contain_items():

def test_when_item_added_cart_contain_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_when_more_than_max_item_than_failed(cart):
    for _ in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

def test_can_get_total_price(cart):
    cart.add("Mung")
    cart.add("Rajma")

    price_map = {"Mung": 100, "Rajma": 80}
    assert cart.get_total_price(price_map) == 180
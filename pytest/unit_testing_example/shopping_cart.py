from typing import List

class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)
        print(self.items)

    def size(self) -> List[str]:    
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
            print(total_price)
        return total_price

# if __name__ == "__main__":
#     cart = ShoppingCart(max_size=5)
#     cart.add("Mung")
#     cart.add("Rajma")
    
#     price_map = {
#         "Mung": 1.5,
#         "Rajma": 2.0
#     }
    
#     total_price = cart.get_total_price(price_map)
#     print(f"Total price: {total_price}")
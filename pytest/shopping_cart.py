from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add(self, item: str):
        self.items.append(item)

    def size(self) -> List[str]:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        pass

    def get_total_price(self, price_map):
        pass



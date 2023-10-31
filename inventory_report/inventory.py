from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self,
                 data: Optional[list[Product]] = None) -> None:
        if data is not None:
            self.data = data

    @property
    def data(self) -> list[Product]:
        return self.data

    @data.setter
    def data(self) -> None:
        self.data: list[Product] = []

    def add_data(self, data: list[Product]) -> None:
        # essa linha substitui o for
        # self.data.extend(data)
        for product in data:
            self.data.append(product)

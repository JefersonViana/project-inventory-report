from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self,
                 data: Optional[list[Product]] = None) -> None:
        self.__data = data or []

    @property
    def data(self) -> list[Product]:
        return self.__data

    def add_data(self, data: list[Product]) -> None:
        # essa linha substitui o for
        # self.data.extend(data)
        for product in data:
            self.data.append(product)

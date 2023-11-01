from inventory_report.inventory import Inventory
from datetime import datetime
from collections import Counter
from typing import Any


class SimpleReport:
    def __init__(self) -> None:
        self.inventories: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def find_empresa(self, inventory: Inventory, fixed: int):
        empresa: Any = ""
        fix = fixed
        if len(inventory.data) > fix:
            current_empresa = Counter(
                [product.company_name for product in inventory.data]
            )
            empresa = max(current_empresa, key=current_empresa.get)
            fix = current_empresa[empresa]
        return (empresa, fix)

    def generate(self) -> str:
        empresa = ""
        fixed = 0
        expiration = datetime.strptime("9999-12-31", "%Y-%m-%d")
        manufacturing = datetime.strptime("9999-12-31", "%Y-%m-%d")
        for inventory in self.inventories:
            for product in inventory.data:
                current_date = datetime.strptime(product.manufacturing_date,
                                                 "%Y-%m-%d")
                current_date_ex = datetime.strptime(product.expiration_date,
                                                    "%Y-%m-%d")
                if current_date < manufacturing:
                    manufacturing = current_date

                if current_date_ex > datetime.now() and (
                    current_date_ex < expiration
                ):
                    expiration = current_date_ex

            new_empresa, count = self.find_empresa(inventory, fixed)
            if fixed < count:
                empresa = new_empresa

        return (
            f"Oldest manufacturing date: {manufacturing.date()}\n"
            f"Closest expiration date: {expiration.date()}\n"
            f"Company with the largest inventory: {empresa}\n"
        )

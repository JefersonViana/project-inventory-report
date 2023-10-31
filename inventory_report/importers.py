from typing import Dict, Type
from inventory_report.product import Product
import abc
import json


class Importer(abc.ABC):
    def __init__(self, path: str) -> None:
        self.path = path
        self.data: list[Product] = []

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        return self.data


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            self.data = [Product(**product) for product in json.load(file)]

        return self.data


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

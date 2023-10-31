from typing import Dict, Type
from inventory_report.product import Product
import abc


class Importer(abc.ABC):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path
        self._import_data: list[Product] = []

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        return self._import_data


class JsonImporter(Importer):
    pass


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

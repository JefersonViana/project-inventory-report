from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    # ['inventory_report/data/inventory.csv', 'inventory_report/data/inventory.json']
    # simple
    # path_test = ['inventory_report/data/inventory.csv', 'inventory_report/data/inventory.json']
    # type_test = 'simple'
    csv_inventory = Inventory()  # lista de produtos
    json_inventory = Inventory()  # lista de produtos
    for path in file_paths:
        if '.csv' in path:
            csv_importer = CsvImporter(path)  # cria lista de produtos
            csv_inventory.add_data(csv_importer.import_data())  # adicionando a lista de produtos no inventario csv
        elif '.json' in path:
            json_importer = JsonImporter(path)
            json_inventory.add_data(json_importer.import_data())
    if report_type == 'simple':
        simple_report = SimpleReport()
        simple_report.add_inventory(csv_inventory)
        simple_report.add_inventory(json_inventory)
        return_text = simple_report.generate()
        return return_text
    elif report_type == 'complete':
        complete_report = CompleteReport()
        complete_report.add_inventory(csv_inventory)
        complete_report.add_inventory(json_inventory)
        return_text = complete_report.generate()
        return return_text
    else:
        raise ValueError("Report type is invalid.")

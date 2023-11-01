from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def create_report(
        csv_inventory: Inventory,
        json_inventory: Inventory,
        report_type: str
) -> str:
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


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    csv_inventory = Inventory()
    json_inventory = Inventory()
    for path in file_paths:
        if '.csv' in path:
            csv_importer = CsvImporter(path)
            csv_inventory.add_data(csv_importer.import_data())
        elif '.json' in path:
            json_importer = JsonImporter(path)
            json_inventory.add_data(json_importer.import_data())
    return create_report(csv_inventory, json_inventory, report_type)


# print(process_report_request(["tests/mocks/inventory.csv"], "simple"))

from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.inventory import Inventory
# from inventory_report.product import Product


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        dict_empresas: dict[str, int] = dict()
        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in dict_empresas:
                    dict_empresas[product.company_name] += 1
                else:
                    dict_empresas[product.company_name] = 1
        return_text = f"{super().generate()}Stocked products by company:\n"
        for empresa in dict_empresas:
            return_text += f"- {empresa}: {dict_empresas[empresa]}\n"

        return return_text

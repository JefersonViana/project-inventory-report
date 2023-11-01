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


# product1 = Product('1', 'iusto', 'Gomes Mor', '2023-10-15', '2023-12-13', 'ABCD', 'instrução 1')
# product2 = Product('2', 'sapiente', 'Gomes Moraes Ltda.', '2023-10-15', '2023-12-13', 'ABCD', 'instrução 2')
# product3 = Product('3', 'natus', 'Gomes Moraes Ltda.', '2023-10-15', '2023-10-15', 'ABCD', 'instrução 3')
# product4 = Product('4', 'doloribus', 'Gomes Moraes Ltda. LIMITED', '2023-09-15', '2023-11-11', 'ABCD', 'instrução 4')
# produtos = [product1, product2, product3, product4]
# inventory = Inventory(produtos)
# complete_report = CompleteReport()
# complete_report.add_inventory(inventory)
# print(complete_report.generate())

from inventory_report.product import Product


def test_product_report(capsys) -> None:
    product = Product("1", "product1", "company_fake1",
                      "2020", "2030", "10", "18")
    print(product)
    captured = capsys.readouterr()
    assert captured.out == ("The product 1 - product1 with serial number "
                            "10 manufactured on 2020 by the company "
                            "company_fake1 valid until 2030 must be stored "
                            "according to the following instructions: 18.\n")

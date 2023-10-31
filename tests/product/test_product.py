from inventory_report.product import Product


def test_create_product() -> None:
    product = Product("1", "product1", "company_fake1", "2020",
                      "2030", "10", "18")

    assert product.id == "1"
    assert product.product_name == "product1"
    assert product.company_name == "company_fake1"
    assert product.manufacturing_date == "2020"
    assert product.expiration_date == "2030"
    assert product.serial_number == "10"
    assert product.storage_instructions == "18"

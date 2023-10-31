from inventory_report.product import Product
import pytest


@pytest.mark.parametrize(
        "input, expected",
        [
            (
                ("1", "product1", "company_fake1", "2020", "2030", "10", "18"),
                ("1", "product1", "company_fake1", "2020", "2030", "10", "18"),
            ),
            (
                ("2", "product2", "company_fake2", "2010", "2015", "55", "25"),
                ("2", "product2", "company_fake2", "2010", "2015", "55", "25"),
            ),
            (
                ("3", "product3", "company_fake3", "2008", "2025", "11", "32"),
                ("3", "product3", "company_fake3", "2008", "2025", "11", "32"),
            ),
            (
                ("4", "product4", "company_fake4", "2020", "2030", "75", "77"),
                ("4", "product4", "company_fake4", "2020", "2030", "75", "77"),
            ),
        ]
)
def test_create_product(input: dict[str, str],
                        expected: dict[str, str]) -> None:
    (id, product_name, company_name, manufacturing_date,
     expiration_date, serial_number, storage_instructions) = input
    (expected_id, expected_product_name,
     expected_company_name, expected_manufacturing_date,
     expected_expiration_date,
     expected_serial_number, expected_storage_instructions) = expected
    product = Product(
        id, product_name, company_name, manufacturing_date, expiration_date,
        serial_number, storage_instructions)

    assert product.id == expected_id
    assert product.product_name == expected_product_name
    assert product.company_name == expected_company_name
    assert product.manufacturing_date == expected_manufacturing_date
    assert product.expiration_date == expected_expiration_date
    assert product.serial_number == expected_serial_number
    assert product.storage_instructions == expected_storage_instructions

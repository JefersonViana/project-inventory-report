from inventory_report.product import Product
import pytest
from typing import Tuple


@pytest.mark.parametrize(
        "input, expected",
        [
            (
                ("1", "product1", "company_fake1", "2020", "2030", "10", "18"),
                ("The product 1 - product1 with serial number "
                 "10 manufactured on 2020 by the company "
                 "company_fake1 valid until 2030 must be stored "
                 "according to the following instructions: 18.\n"),
            )
        ]
)
def test_product_report(capsys,
                        input: Tuple[str, str, str, str, str, str, str],
                        expected: str
                        ) -> None:
    (id, product_name, company_name, manufacturing_date,
     expiration_date, serial_number, storage_instructions) = input
    product = Product(
        id, product_name, company_name, manufacturing_date, expiration_date,
        serial_number, storage_instructions)

    print(product)
    captured = capsys.readouterr()
    assert captured.out == expected

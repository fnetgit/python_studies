import pytest
from inventory import Product, InsufficientStockException


@pytest.fixture
def default_product() -> Product:
    return Product(product_id="001", name="caixa de leite", price=8.99, quantity=10)


@pytest.mark.parametrize("amount_to_add, expected_qty", [(5, 15), (10, 20), (100, 110)])
def test_increase_stock(default_product, amount_to_add, expected_qty):
    default_product.increase_stock(amount_to_add)
    assert default_product.quantity == expected_qty


def test_decrease_stock_quantity(default_product):
    default_product.decrease_stock(1)
    assert default_product.quantity == 9


def test_decrease_exceeds_current_stock(default_product):
    with pytest.raises(InsufficientStockException):
        default_product.decrease_stock(15)


def test_increase_stock_invalid_value(default_product):
    with pytest.raises(ValueError, match="maior que zero"):
        default_product.increase_stock(-5)

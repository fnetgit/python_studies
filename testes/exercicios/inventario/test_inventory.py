import pytest
from inventory import (
    InsufficientStockException,
    InventoryService,
    Product,
    ProductNotFoundException,
)

# uv add pytest-cov (plugin para ver a cobertura dos testes)
# pytest --cov=inventario test_inventory.py ()

# coverage html
# microsoft-edge coverage_html_report/index.html


def test_product_initialization():
    p = Product("001", "caixa de leite", 4.50, 20)
    assert p.product_id == "001"
    assert p.name == "caixa de leite"
    assert p.price == 4.50
    assert p.quantity == 20


def test_create_item_with_no_id():
    with pytest.raises(ValueError):
        Product("", "caixa de leite", 4.50, 20)


def test_create_item_with_no_name():
    with pytest.raises(ValueError):
        Product("001", "", 4.50, 20)


def test_create_item_with_zero_price():
    with pytest.raises(ValueError):
        Product("001", "caixa de leite", 0.0, 20)


def test_create_item_with_negative_price():
    with pytest.raises(ValueError):
        Product("001", "caixa de leite", -4.50, 20)


def test_create_item_with_negative_amount():
    with pytest.raises(ValueError):
        Product("001", "caixa de leite", 4.50, -20)


@pytest.fixture
def default_product() -> Product:
    return Product(product_id="001", name="caixa de leite", price=8.99, quantity=10)


@pytest.fixture
def default_inventory_service() -> InventoryService:
    return InventoryService()


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


def test_decrease_stock_zero(default_product):
    with pytest.raises(ValueError):
        default_product.decrease_stock(0)


def test_decrease_stock_invalid_value(default_product):
    with pytest.raises(ValueError):
        default_product.decrease_stock(-5)


def test_increase_stock_invalid_value(default_product):
    with pytest.raises(ValueError, match="maior que zero"):
        default_product.increase_stock(-5)


def test_register_product_success(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    assert (
        default_inventory_service.retrieve_product(default_product.product_id)
        == default_product
    )


def test_product_is_already_registered(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    with pytest.raises(ValueError):
        default_inventory_service.register_product(default_product)


def test_retrieve_product_success(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    assert (
        default_inventory_service.retrieve_product(default_product.product_id)
        == default_product
    )


def test_retrieve_product_failure(default_inventory_service, default_product):
    with pytest.raises(ProductNotFoundException):
        default_inventory_service.retrieve_product(default_product.product_id)


def test_process_dispatch_success(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    default_inventory_service.process_dispatch(default_product.product_id, 10)


def test_process_dispatch_error_amount_exceeds_stock(
    default_inventory_service, default_product
):
    with pytest.raises(InsufficientStockException):
        default_inventory_service.register_product(default_product)
        default_inventory_service.process_dispatch(default_product.product_id, 11)


def test_process_dispatch_amount_zero(default_inventory_service, default_product):
    with pytest.raises(ValueError):
        default_inventory_service.register_product(default_product)
        default_inventory_service.process_dispatch(default_product.product_id, 0)


def test_process_dispatch_amount_negative(default_inventory_service, default_product):
    with pytest.raises(ValueError):
        default_inventory_service.register_product(default_product)
        default_inventory_service.process_dispatch(default_product.product_id, -1)


def test_get_inventory_alerts_stock_normal(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    assert default_inventory_service.get_inventory_alerts(10) == []


def test_get_inventory_alerts_low_stock(default_inventory_service, default_product):
    default_inventory_service.register_product(default_product)
    assert default_inventory_service.get_inventory_alerts(11) == [default_product]

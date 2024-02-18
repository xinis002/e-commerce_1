import pytest

@pytest.fixture
def product_fixture():
    return Product("Test Product", "This is a test product", 99.99, 10)

@pytest.fixture
def category_fixture(product_fixture):
    return Category("Test Category", "This is a test category", [product_fixture])

def test_product_initialization(product_fixture):
    assert product_fixture.name == "Test Product"
    assert product_fixture.description == "This is a test product"
    assert product_fixture.price == 99.99
    assert product_fixture.quantity == 10

def test_category_initialization(category_fixture):
    assert category_fixture.name == "Test Category"
    assert category_fixture.description == "This is a test category"
    assert len(category_fixture.products) == 1

def test_total_categories(category_fixture):
    assert Category.total_categories > 0

def test_total_unique_products(category_fixture):
    assert len(Category.total_unique_products) > 0
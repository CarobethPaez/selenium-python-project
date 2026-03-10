# tests/test_inventory.py
import pytest
from pages.inventory_page import InventoryPage

class TestInventory:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_inventory_page_loads(self, logged_in_driver):
        inventory_page = InventoryPage(logged_in_driver)
        assert inventory_page.is_loaded() 

    @pytest.mark.regression
    def test_inventory_shows_6_products(self, logged_in_driver):
        """Test: el inventario muestra 6 productos"""
        inventory_page = InventoryPage(logged_in_driver)
        assert inventory_page.get_inventory_items_count() == 6

    @pytest.mark.regression
    def test_add_product_updates_cart(self, logged_in_driver):
        """Test: agregar producto actualiza el carrito"""
        inventory_page = InventoryPage(logged_in_driver)
        inventory_page.add_product_to_cart('sauce-labs-backpack')
        assert inventory_page.get_cart_count() == 1
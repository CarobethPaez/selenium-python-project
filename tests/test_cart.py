# tests/test_cart.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCart:
    
    def test_add_product_to_cart(self, driver):
        """Test: agregar un producto al carrito"""
        # Arrange
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        # Act
        login_page.visit()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_product_to_cart('sauce-labs-backpack')
        
        # Assert
        assert inventory_page.get_cart_count() == 1
    
    def test_cart_shows_added_products(self, driver):
        """Test: el carrito muestra los productos agregados"""
        # Arrange
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        # Act
        login_page.visit()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_product_to_cart('sauce-labs-backpack')
        inventory_page.go_to_cart()
        
        # Assert
        assert cart_page.is_loaded()
        assert cart_page.get_cart_items_count() == 1
    
    def test_inventory_shows_6_products(self, driver):
        """Test: el inventario muestra 6 productos"""
        # Arrange
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        # Act
        login_page.visit()
        login_page.login('standard_user', 'secret_sauce')
        
        # Assert
        assert inventory_page.get_inventory_items_count() == 6
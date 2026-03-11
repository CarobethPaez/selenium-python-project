# tests/test_checkout.py
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:

    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_complete_purchase_flow(self, logged_in_driver):
       """Test E2E: flujo completo de compra"""
    # Arrange
       inventory_page = InventoryPage(logged_in_driver)
       checkout_page = CheckoutPage(logged_in_driver)
    
    # Act — agregar producto al carrito
       inventory_page.add_product_to_cart('sauce-labs-backpack')
    
    # Navegar directamente al checkout
       logged_in_driver.get('https://www.saucedemo.com/checkout-step-one.html')
       print(f'\n URL actual: {logged_in_driver.current_url}')
    
    # Act — llenar información personal
       checkout_page.fill_personal_info('Carobeth', 'Paez', '12345')
       checkout_page.click_continue()
    
    # Act — finalizar compra
       checkout_page.click_finish()
    
    # Assert
       assert checkout_page.is_order_complete()
       assert 'Thank you for your order' in checkout_page.get_complete_title()

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_empty_fields(self, logged_in_driver):
        """Test: checkout con campos vacíos"""
        # Arrange
        inventory_page = InventoryPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        checkout_page = CheckoutPage(logged_in_driver)
        
        # Act
        inventory_page.add_product_to_cart('sauce-labs-backpack')
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.click_continue()
        
        # Assert
        assert 'First Name is required' in checkout_page.get_error_message()

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_missing_postal_code(self, logged_in_driver):
        """Test: checkout sin código postal"""
        # Arrange
        inventory_page = InventoryPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        checkout_page = CheckoutPage(logged_in_driver)
    
        # Act
        inventory_page.add_product_to_cart('sauce-labs-backpack')
        inventory_page.go_to_cart()
        cart_page.click_checkout()
    
        # Llenar solo nombre y apellido, sin postal code
        checkout_page.type_text(checkout_page.FIRST_NAME, 'Carobeth')
        checkout_page.type_text(checkout_page.LAST_NAME, 'Paez')
        checkout_page.click_continue()
    
        # Assert
        assert 'Postal Code is required' in checkout_page.get_error_message()


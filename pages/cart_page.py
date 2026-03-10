# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    
    # Selectores
    TITLE = (By.CLASS_NAME, 'title')
    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CONTINUE_SHOPPING = (By.ID, 'continue-shopping')
    
    def is_loaded(self) -> bool:
        """Verificar que la página está cargada"""
        return 'cart' in self.get_current_url()
    
    def get_cart_items_count(self) -> int:
        """Obtener la cantidad de items en el carrito"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def click_checkout(self):
        """Click en el botón de checkout"""
        self.click(self.CHECKOUT_BUTTON)
    
    def continue_shopping(self):
        """Click en continuar comprando"""
        self.click(self.CONTINUE_SHOPPING)
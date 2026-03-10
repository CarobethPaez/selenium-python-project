# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    
    # Selectores
    TITLE = (By.CLASS_NAME, 'title')
    INVENTORY_ITEMS = (By.CLASS_NAME, 'inventory_item')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    
    def get_title(self) -> str:
        """Obtener el título de la página"""
        return self.get_text(self.TITLE)
    
    def is_loaded(self) -> bool:
        """Verificar que la página está cargada"""
        return 'inventory' in self.get_current_url()
    
    def get_inventory_items_count(self) -> int:
        """Obtener la cantidad de productos"""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)
    
    def add_product_to_cart(self, product_name: str):
        """Agregar un producto al carrito por nombre"""
        button_locator = (
            By.CSS_SELECTOR,
            f'[data-test="add-to-cart-{product_name}"]'
        )
        self.click(button_locator)
    
    def get_cart_count(self) -> int:
        """Obtener la cantidad de items en el carrito"""
        try:
            badge = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0
    
    def go_to_cart(self):
        """Navegar al carrito"""
        self.click(self.CART_ICON)
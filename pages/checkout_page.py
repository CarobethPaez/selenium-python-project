# pages/checkout_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    
    # Selectores — Step 1 (información personal)
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_TITLE = (By.CLASS_NAME, 'complete-header')
    
    # Selectores — Step 2 (resumen)
    FINISH_BUTTON = (By.ID, 'finish')
    SUMMARY_TOTAL = (By.CLASS_NAME, 'summary_total_label')
    
    # Selectores — Confirmación
    COMPLETE_TITLE = (By.CLASS_NAME, 'complete-header')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')
    
    def is_loaded(self) -> bool:
        """Verificar que la página está cargada"""
        return 'checkout-step-one' in self.get_current_url()
    
    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str):
        """Llenar información personal"""
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
    
    def click_continue(self):
        """Click en continuar"""
        self.click(self.CONTINUE_BUTTON)
    
    def click_finish(self):
        """Click en finalizar compra"""
        self.click(self.FINISH_BUTTON)
    
    def get_error_message(self) -> str:
        """Obtener mensaje de error"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def get_order_total(self) -> str:
        """Obtener el total de la orden"""
        return self.get_text(self.SUMMARY_TOTAL)
    
    def get_complete_title(self) -> str:
        """Obtener título de confirmación"""
        return self.get_text(self.COMPLETE_TITLE)
    
    def is_order_complete(self) -> bool:
        """Verificar que la orden fue completada"""
        return 'checkout-complete' in self.get_current_url()
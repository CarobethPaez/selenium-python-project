# pages/base_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """
    Clase base para todos los Page Objects
    Contiene métodos comunes reutilizables
    """
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator: tuple):
        """Encontrar un elemento esperando a que esté visible"""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def click(self, locator: tuple):
        """Click en un elemento"""
        self.find_element(locator).click()
    
    def type_text(self, locator: tuple, text: str):
        """Escribir texto en un elemento"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: tuple) -> str:
        """Obtener texto de un elemento"""
        return self.find_element(locator).text
    
    def is_displayed(self, locator: tuple) -> bool:
        """Verificar si un elemento está visible"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def get_current_url(self) -> str:
        """Obtener la URL actual"""
        return self.driver.current_url
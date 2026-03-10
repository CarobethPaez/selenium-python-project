# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

BASE_URL = 'https://www.saucedemo.com'

class LoginPage(BasePage):
    
    # Selectores
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    
    def visit(self):
        """Navegar a la página de login"""
        self.driver.get(BASE_URL)
    
    def enter_username(self, username: str):
        """Ingresar nombre de usuario"""
        self.type_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """Ingresar contraseña"""
        self.type_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click en el botón de login"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str):
        """Método completo de login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Obtener el mensaje de error"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Verificar si el error está visible"""
        return self.is_displayed(self.ERROR_MESSAGE)
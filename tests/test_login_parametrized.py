# tests/test_login_parametrized.py
import pytest
from pages.login_page import LoginPage

# Datos de prueba
INVALID_CREDENTIALS = [
    ('invalid_user', 'secret_sauce', 'Username and password do not match'),
    ('locked_out_user', 'secret_sauce', 'Sorry, this user has been locked out'),
    ('', '', 'Username is required'),
    ('standard_user', '', 'Password is required'),
]

class TestLoginParametrized:
    
    @pytest.mark.parametrize('username, password, expected_error', INVALID_CREDENTIALS)
    def test_login_error_messages(self, driver, username, password, expected_error):
        """Test parametrizado: verificar mensajes de error"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()
        
        # Act
        if username:
            login_page.enter_username(username)
        if password:
            login_page.enter_password(password)
        login_page.click_login()
        
        # Assert
        assert expected_error in login_page.get_error_message()
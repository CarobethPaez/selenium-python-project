# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_login_happy_path(self, driver):
        """Test: login con credenciales válidas"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()

        # Act
        login_page.login('standard_user', 'secret_sauce')

        # Assert
        assert '/inventory' in driver.current_url

    def test_login_invalid_credentials(self, driver):
        """Test: login con credenciales inválidas"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()

        # Act
        login_page.login('invalid_user', 'wrong_password')

        # Assert
        assert login_page.is_error_displayed()

    def test_login_empty_fields(self, driver):
        """Test: login con campos vacíos"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()

        # Act
        login_page.click_login()

        # Assert
        assert 'Username is required' in login_page.get_error_message()

    def test_login_locked_user(self, driver):
        """Test: login con usuario bloqueado"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()

        # Act
        login_page.login('locked_out_user', 'secret_sauce')

        # Assert
        assert 'Sorry, this user has been locked out' in login_page.get_error_message()

    def test_login_empty_password(self, driver):
        """Test: login con password vacío"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.visit()

        # Act
        login_page.enter_username('standard_user')
        login_page.click_login()

        # Assert
        assert 'Password is required' in login_page.get_error_message()

# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_happy_path(self, driver):
        """Test crítico: login con credenciales válidas"""
        login_page = LoginPage(driver)
        login_page.visit()
        login_page.login('standard_user', 'secret_sauce')
        assert '/inventory' in driver.current_url

    @pytest.mark.regression
    @pytest.mark.login
    def test_login_invalid_credentials(self, driver):
        """Test de regresión: login con credenciales inválidas"""
        login_page = LoginPage(driver)
        login_page.visit()
        login_page.login('invalid_user', 'wrong_password')
        assert login_page.is_error_displayed()

    @pytest.mark.regression
    @pytest.mark.login
    def test_login_empty_fields(self, driver):
        """Test: login con campos vacíos"""
        login_page = LoginPage(driver)
        login_page.visit()
        login_page.click_login()
        assert 'Username is required' in login_page.get_error_message()

    @pytest.mark.regression
    @pytest.mark.login
    def test_login_locked_user(self, driver):
        """Test: login con usuario bloqueado"""
        login_page = LoginPage(driver)
        login_page.visit()
        login_page.login('locked_out_user', 'secret_sauce')
        assert 'Sorry, this user has been locked out' in login_page.get_error_message()

    @pytest.mark.regression
    @pytest.mark.login
    def test_login_empty_password(self, driver):
        """Test: login con password vacío"""
        login_page = LoginPage(driver)
        login_page.visit()
        login_page.enter_username('standard_user')
        login_page.click_login()
        assert 'Password is required' in login_page.get_error_message()
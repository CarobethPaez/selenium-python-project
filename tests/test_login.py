# tests/test_login.py
import pytest
from selenium.webdriver.common.by import By

BASE_URL = 'https://www.saucedemo.com'

class TestLogin:
    
    def test_login_happy_path(self, driver):
        """Test: login con credenciales válidas"""
        # Arrange
        driver.get(BASE_URL)
        
        # Act
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        
        # Assert
        assert '/inventory' in driver.current_url
    
    def test_login_invalid_credentials(self, driver):
        """Test: login con credenciales inválidas"""
        # Arrange
        driver.get(BASE_URL)
        
        # Act
        driver.find_element(By.ID, 'user-name').send_keys('invalid_user')
        driver.find_element(By.ID, 'password').send_keys('wrong_password')
        driver.find_element(By.ID, 'login-button').click()
        
        # Assert
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_message.is_displayed()
    
    def test_login_empty_fields(self, driver):
        """Test: login con campos vacíos"""
        # Arrange
        driver.get(BASE_URL)
        
        # Act — click sin llenar campos
        driver.find_element(By.ID, 'login-button').click()
        
        # Assert
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert 'Username is required' in error_message.text

    def test_login_locked_user(self, driver):
        """Test: login con usuario bloqueado"""
        # Arrange
        driver.get(BASE_URL)

        # Act
        driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        # Assert
        error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert 'Sorry, this user has been locked out' in error.text

    def test_login_empty_password(self, driver):
        """Test: login con password vacío"""
        # Arrange
        driver.get(BASE_URL)

        # Act
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'login-button').click()

        # Assert
        error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert 'Password is required' in error.text
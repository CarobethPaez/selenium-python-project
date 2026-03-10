# conftest.py
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_configure(config):
    """Configuración global de pytest"""
    config.addinivalue_line(
        "markers", "smoke: Tests críticos"
    )

def pytest_runtest_makereport(item, call):
    """Hook para tomar screenshot cuando falla un test"""
    if call.when == 'call' and call.excinfo is not None:
        # El test falló — tomar screenshot
        driver = item.funcargs.get('driver')
        if driver:
            # Crear carpeta de screenshots si no existe
            os.makedirs('reports/screenshots', exist_ok=True)
            
            # Nombre del screenshot con timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name.replace('/', '_')
            screenshot_path = f'reports/screenshots/{test_name}_{timestamp}.png'
            
            # Tomar screenshot
            driver.save_screenshot(screenshot_path)
            print(f'\n📸 Screenshot guardado: {screenshot_path}')

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def logged_in_driver(driver):
    """Fixture con login ya hecho"""
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.visit()
    login_page.login('standard_user', 'secret_sauce')
    yield driver
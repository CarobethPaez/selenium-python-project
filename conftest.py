import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_runtest_makereport(item, call):
    """Hook para tomar screenshot cuando falla un test"""
    if call.when == 'call' and call.excinfo is not None:
        driver = item.funcargs.get('driver')
        if driver:
            os.makedirs('reports/screenshots', exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name.replace('/', '_')
            screenshot_path = f'reports/screenshots/{test_name}_{timestamp}.png'
            driver.save_screenshot(screenshot_path)
            print(f'\n📸 Screenshot guardado: {screenshot_path}')

def pytest_html_report_title(report):
    """Personalizar el título del reporte"""
    report.title = "Selenium Python — E2E Test Results"

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    # Deshabilitar popups de contraseñas ← nuevo
    options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.password_manager_leak_detection': False
    })
    
    # Headless en CI/CD
    if os.environ.get('CI'):
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
    
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
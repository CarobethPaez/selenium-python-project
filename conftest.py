# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    """
    Fixture que crea y destruye el driver para cada test
    """
    # Configurar opciones de Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Crear driver con WebDriver Manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    # Configurar espera implícita
    driver.implicitly_wait(10)
    
    # Maximizar ventana
    driver.maximize_window()
    
    yield driver  # ← aquí corre el test
    
    # Teardown — cerrar driver después del test
    driver.quit()
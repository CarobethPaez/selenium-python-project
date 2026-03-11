# 🧪 Selenium Python Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-brightgreen)
![pytest](https://img.shields.io/badge/pytest-8-orange)
![Tests](https://img.shields.io/badge/tests-18%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

E2E Testing framework built with Selenium and Python using Page Object Model architecture.

## ✨ Features
- ✅ Page Object Model architecture
- ✅ BasePage with reusable methods
- ✅ Python type hints for better code quality
- ✅ Automatic ChromeDriver management
- ✅ HTML reports with pytest-html
- ✅ Setup and teardown with pytest fixtures
- ✅ Screenshots on test failure
- ✅ Data-Driven Testing with pytest.mark.parametrize
- ✅ Test markers: smoke, regression, login, cart, checkout
- ✅ GitHub Actions CI/CD pipeline

## 🚀 Tech Stack
- **Selenium 4** — E2E Testing framework
- **Python 3.13** — Programming language
- **pytest** — Test framework
- **WebDriver Manager** — Automatic driver management
- **pytest-html** — HTML Reports

## 📁 Project Structure
```
selenium-python-project/
├── .github/
│   └── workflows/
│       └── selenium.yml       # CI/CD pipeline
├── pages/
│   ├── base_page.py           # Base Page Object
│   ├── login_page.py          # Login Page Object
│   ├── inventory_page.py      # Inventory Page Object
│   ├── cart_page.py           # Cart Page Object
│   └── checkout_page.py       # Checkout Page Object
├── tests/
│   ├── test_login.py          # Login tests
│   ├── test_cart.py           # Cart tests
│   ├── test_inventory.py      # Inventory tests
│   ├── test_checkout.py       # Checkout tests
│   └── test_login_parametrized.py  # Parametrized tests
├── utils/
│   └── test_data.py           # Test data
├── reports/                   # Generated reports
├── conftest.py                # pytest fixtures
├── pytest.ini                 # pytest config
└── requirements.txt           # Dependencies
```

## ▶️ How to Run
```bash
# Clone the repository
git clone https://github.com/CarobethPaez/selenium-python-project.git
cd selenium-python-project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run by marker
pytest tests/ -v -m smoke
pytest tests/ -v -m regression
pytest tests/ -v -m login
pytest tests/ -v -m checkout
```

## 📊 Reports
```bash
# Generate HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Open report
# Windows:
start reports/report.html
```

## 🧪 Test Coverage

| Module | Tests | Markers |
|--------|-------|---------|
| Login | 5 | smoke, regression, login |
| Cart | 3 | regression, cart |
| Inventory | 3 | smoke, regression |
| Checkout | 3 | smoke, regression, checkout |
| Login Parametrized | 4 | regression, login |
| **Total** | **18** | |

## 🌐 CI/CD
- ✅ GitHub Actions pipeline
- ✅ Runs on every push to main
- ✅ Headless Chrome in CI
- ✅ HTML report uploaded as artifact
- ✅ Screenshots uploaded on failure
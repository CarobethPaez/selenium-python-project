# 🧪 Selenium Python Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-brightgreen)
![pytest](https://img.shields.io/badge/pytest-8-orange)
![License](https://img.shields.io/badge/license-MIT-green)

E2E Testing framework built with Selenium and Python using Page Object Model architecture.

## ✨ Features
- ✅ Page Object Model architecture
- ✅ Python type hints for better code quality
- ✅ Automatic ChromeDriver management
- ✅ HTML reports with pytest-html
- ✅ Setup and teardown with pytest fixtures
- ✅ Cross-browser testing ready

## 🚀 Tech Stack
- **Selenium 4** — E2E Testing framework
- **Python 3.13** — Programming language
- **pytest** — Test framework
- **WebDriver Manager** — Automatic driver management
- **pytest-html** — HTML Reports

## 📁 Project Structure
```
selenium-python-project/
├── pages/
│   ├── __init__.py
│   └── login_page.py      # Page Objects
├── tests/
│   ├── __init__.py
│   └── test_login.py      # Test files
├── reports/               # Generated reports
├── utils/                 # Utilities
├── conftest.py            # pytest fixtures
├── pytest.ini             # pytest config
└── requirements.txt       # Dependencies
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

# Run specific test file
pytest tests/test_login.py -v
```

## 📊 Reports
```bash
# Generate HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html
```
Reports are automatically generated in the `reports/` folder.

## 🌐 Test Coverage
- ✅ Login Happy Path
- ✅ Login with invalid credentials
- ✅ Login with empty fields
- ✅ Login with locked user
- ✅ Login with empty password
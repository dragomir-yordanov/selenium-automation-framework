Описание

Това е примерен automation testing framework на Python с Selenium WebDriver, Pytest, Page Object Model (POM) и CI/CD с GitHub Actions.

Проектът демонстрира:

Page Object Model за подреден код

Параметризирани тестове с Pytest

HTML репорти (pytest-html)

Headless Chrome за автоматично изпълнение в CI

CI/CD workflow с GitHub Actions за автоматично пускане на тестовете

Branch workflow за QA Automation team

Структура на проекта
automation_framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   └── test_login.py
│
├── .github/
│   └── workflows/tests.yml
├── conftest.py
├── config.json
├── requirements.txt
└── README.md

Инсталация

Клонирай репото:

git clone https://github.com/<your-username>/<your-repo>.git
cd automation_framework


Създай virtual environment и го активирай:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate


Инсталирай зависимостите:

pip install -r requirements.txt

Стартиране на тестовете локално
pytest --html=report.html --self-contained-html


Генерира HTML репорт report.html.

Chrome се стартира headless (без GUI).

GitHub Actions (CI/CD)

Всеки push или pull request към main пуска тестовете автоматично.

Генерира HTML репорт и го качва като artifact.

Headless Chrome се използва за стабилно изпълнение на CI.

Branch workflow за QA Automation
Branch	Цел
main	Стабилен branch с минали тестове.
develop	Интеграционен branch, където се сливат feature branch-овете.
feature/<name>	Нови функционалности или тестове.
bugfix/<name>	Поправки на тестове или грешки.

Примерен workflow:

Създаваш feature branch:

git checkout -b feature/login-tests


Локално пускаш тестовете:

pytest --html=report.html --self-contained-html


Push на branch и създаване на Pull Request към develop.

CI/CD workflow автоматично стартира тестовете → проверява статуса.

Merge към develop → после към main когато всичко е стабилно.

Конфигурация

config.json съдържа:

{
  "base_url": "https://www.saucedemo.com/",
  "username": "standard_user",
  "password": "secret_sauce"
}

Технологии

Python 3.11

Selenium WebDriver

Pytest

Pytest-html

WebDriver Manager

GitHub Actions

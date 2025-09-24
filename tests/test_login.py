import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config_reader import load_config

config = load_config()

@pytest.mark.parametrize("username,password,expected", [
    (config["username"], config["password"], True),       # валидни
    ("wrong_user", "secret_sauce", False),                # грешно потребителско
    ("standard_user", "wrong_pass", False)                # грешна парола
])
def test_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_page(config["base_url"])
    login_page.login(username, password)

    if expected:
        assert inventory_page.is_opened()
        assert inventory_page.get_title() == "Products"
    else:
        assert not inventory_page.is_opened()

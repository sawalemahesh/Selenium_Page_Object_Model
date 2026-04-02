import json
import pytest
from pages.login_page import LoginPage

def load_test_data():
    with open("testdata/test_data.json") as f:
        return json.load(f)


def test_login_valid(driver):
    data = load_test_data()
    login_page = LoginPage(driver)
    login_page.login(data["valid"]["username"], data["valid"]["password"])
    assert "dashboard" in driver.current_url.lower()

@pytest.mark.parametrize("user_data", load_test_data()["invalid"])
def test_login_invalid(driver, user_data):
    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    # Check error message or login failure
    assert "dashboard" not in driver.current_url.lower()

@pytest.mark.parametrize("user_data", load_test_data()["invalid"])
def test_login_invalid(driver, user_data):
    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    error = login_page.get_error_message()
    assert "Invalid credentials" in error

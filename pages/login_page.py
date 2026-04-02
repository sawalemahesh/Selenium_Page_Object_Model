from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.USERNAME)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BTN)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MSG)
        ).text
from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
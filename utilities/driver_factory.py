from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.config_reader import get_browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver():
    browser = get_browser()


    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver
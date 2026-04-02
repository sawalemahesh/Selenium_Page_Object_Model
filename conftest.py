import pytest
from utilities.driver_factory import get_driver
from utilities.config_reader import get_base_url

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(get_base_url())
    yield driver
    driver.quit()
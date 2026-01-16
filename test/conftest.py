import pytest
from drivers.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    if driver:
        driver.quit()

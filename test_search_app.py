import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from search_app import driver_setup, SeleniumUtilities, search_logic


@pytest.fixture(scope="module")
def browser_instance():
    driver = driver_setup()
    yield driver
    driver.quit()
    print("Browser closed by pytest fixture")


def test_driver_setup_works(browser_instance):
    assert browser_instance is not None
    assert browser_instance.name == "chrome"

def test_helper_class_works(browser_instance):
    browser_instance.get("https://www.google.com")
    util = SeleniumUtilities(browser_instance, 5)
    
    search_bar = util.find_clickable_element((By.NAME, "q"))
    assert search_bar.is_displayed()

def test_load_page_success(browser_instance):
    driver = browser_instance
    driver.get("https://www.google.com")
    util = SeleniumUtilities(driver, 5)
    
    search_locator = (By.NAME, "q")
    search = "DataArt"
    link_locator = (By.PARTIAL_LINK_TEXT, search)
    
    searchbar = util.find_clickable_element((By.NAME, "q"))

    search_logic(driver, util, search_locator, link_locator, search)
    
    WebDriverWait(driver, 5).until(
        EC.staleness_of(searchbar)
    )


import pytest
from selenium.webdriver.common.by import By
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

# def test_app_main_logic_success(browser_instance):
#     driver = browser_instance
#     util = SeleniumUtilities(driver, 5)
    
#     search_locator = (By.NAME, "q")
#     search = "DataArt"
#     link_locator = (By.PARTIAL_LINK_TEXT, search)

#     result = search_logic(driver, util, search_locator, link_locator, search)
#     assert result is True

def test_app_main_logic_failure_on_bad_link(browser_instance):

    driver = browser_instance
    util = SeleniumUtilities(driver, 5)
    
    search_locator = (By.NAME, "q")
    bad_link_locator = (By.PARTIAL_LINK_TEXT, "NON_EXISTENT_LINK_12345")
    
    result = search_logic(driver, util, search_locator, bad_link_locator)
    assert result is False
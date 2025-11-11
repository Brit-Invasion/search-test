import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class SeleniumUtilities:
    """
    Wrapper class that handles timeouts
    """
    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_clickable_element(self, locator):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException as e:
            print(f"Timeout: Element '{locator[1]}' wasn't find on page after {self.wait._timeout}s.")
            raise e


def driver_setup():
    print("Updating chromedriver...")
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1000,800")
    
    driver = webdriver.Chrome(service=service, options=options)
    print("Driver is active")
    return driver

def search_logic(driver, util, search_locator, link_locator, search="DataArt"):
    try:
        url = "https://www.google.com"
        driver.get(url)

        searchbar = util.find_clickable_element(search_locator)
        searchbar.send_keys(search + Keys.ENTER)

        link = util.find_clickable_element(link_locator)
        link.click()

        return search in driver.title
    
    except TimeoutException:
        return False
    except Exception as e:
        print(f"An unexpected error occurred in search logic: {e}")
        return False


if __name__ == '__main__':  
    driver = None
    try:

        driver = driver_setup()
        util = SeleniumUtilities(driver, 15)
        
        searchbar_locator = (By.NAME, "q")
        search = "DataArt"
        link_locator = (By.PARTIAL_LINK_TEXT, search)

        success = search_logic(driver, util, searchbar_locator, link_locator, search)

        if success:
            print(f"Successfully found link: {driver.title}")
        else:
            print("Search logic failure.")

        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if driver:
            driver.quit()
            print("Browser closed")
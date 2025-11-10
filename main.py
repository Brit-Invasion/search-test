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
        except TimeoutException:
            print(f"Timeout: Element '{locator[1]}' wasn't find on page after {self.wait._timeout}s.")


def driver_setup():
    print("Updating chromedriver...")
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    print("Driver is active")

    return driver

def search(searchbar_locator, link_locator):
    searchbar = util.find_clickable_element(searchbar_locator)
    searchbar.send_keys("DataArt" + Keys.ENTER)

    link = util.find_clickable_element(link_locator)
    link.click()

    print(f"Successfully found link: {driver.title}")



if __name__ == '__main__':  
    try:

        driver = driver_setup()
        util = SeleniumUtilities(driver, 15)
        
        url = "https://www.google.com"
        driver.get(url)

        searchbar_locator = (By.NAME, "")
        link_locator = (By.PARTIAL_LINK_TEXT, "DataArt")

        search(searchbar_locator, link_locator)

        time.sleep(5)

        driver.quit()
        print("Browser closed")

    except Exception as e:
        print(f"Error: {e}")
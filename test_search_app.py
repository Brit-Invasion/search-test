import pytest
from selenium.webdriver.common.by import By

# --- Импортируем "компоненты" твоего приложения ---
from search_app import driver_setup, SeleniumUtilities, search_logic

@pytest.fixture(scope="module")
def browser_instance():
    """
    Это "фикстура" Pytest. 
    Она запускается один раз для всех тестов в этом файле.
    Это наш аналог setUp/tearDown.
    """
    driver = driver_setup()  # <--- Используем твою функцию
    yield driver
    # Код после 'yield' - это tearDown
    driver.quit()
    print("Browser closed by pytest fixture")


# --- Тесты ---
# Названия тестов должны начинаться с test_

def test_driver_setup_works(browser_instance):
    """
    Тест 1: Проверяем, что твоя функция driver_setup() 
    вообще возвращает рабочий драйвер.
    """
    assert browser_instance is not None
    assert browser_instance.name == "chrome"

def test_helper_class_works(browser_instance):
    """
    Тест 2: Проверяем, что твой класс SeleniumUtilities работает.
    """
    # browser_instance - это driver, который пришел из фикстуры
    browser_instance.get("https://www.google.com")
    util = SeleniumUtilities(browser_instance, 5) # <--- Используем твой класс
    
    search_bar = util.find_clickable_element((By.NAME, "q"))
    assert search_bar.is_displayed()

# def test_app_main_logic_success(browser_instance):
#     """
#     Тест 3: Главный E2E-тест твоего скрипта.
#     Проверяем успешный сценарий.
#     """
#     driver = browser_instance
#     util = SeleniumUtilities(driver, 10)
    
#     search_locator = (By.NAME, "q")
#     search = "DataArt"
#     link_locator = (By.PARTIAL_LINK_TEXT, search)

#     # --- Вызываем твою главную функцию ---
#     result = search_logic(driver, util, search_locator, link_locator, search)
    
#     # --- Проверяем (Assert) результат ---
#     assert result is True

def test_app_main_logic_failure_on_bad_link(browser_instance):
    """
    Тест 4: Проверяем, что твой скрипт вернет False (не упадет),
    если нужная ссылка не найдена.
    """
    driver = browser_instance
    util = SeleniumUtilities(driver, 5) # Короткий таймаут
    
    search_locator = (By.NAME, "q")
    bad_link_locator = (By.PARTIAL_LINK_TEXT, "NON_EXISTENT_LINK_12345")
    
    # --- Вызываем твою главную функцию ---
    result = search_logic(driver, util, search_locator, bad_link_locator)
    
    # --- Проверяем (Assert) результат ---
    assert result is False
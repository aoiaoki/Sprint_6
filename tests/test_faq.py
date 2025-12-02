import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COOKIE_ACCEPT = (By.CSS_SELECTOR, ".App_CookieConsent__1yUIN button")

def close_cookie_banner(driver):

    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(COOKIE_ACCEPT)).click()
    except:
        pass

@pytest.mark.parametrize("index", range(8))
def test_faq_answers(driver, index):
    page = MainPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/")

    close_cookie_banner(driver)


    element = driver.find_element(*page.FAQ_QUESTION(index))
    driver.execute_script("arguments[0].click();", element)


    assert page.get_text(page.FAQ_ANSWER(index)) != ""

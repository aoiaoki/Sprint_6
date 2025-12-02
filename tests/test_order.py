import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.final_page import FinalPage

COOKIE_ACCEPT = (By.CSS_SELECTOR, ".App_CookieConsent__1yUIN button")

def close_cookie_banner(driver):
    try:
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(COOKIE_ACCEPT)
        ).click()
    except:
        pass


data_sets = [
    {
        "name": "Иван",
        "surname": "Петров",
        "address": "Москва, Льва Толстого 16",
        "metro": "Парк культуры",
        "phone": "89990000001",
        "date": "31.12.2025",
        "rent": "двое суток",
        "colors": ["black"]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "address": "Москва, Тверская 5",
        "metro": "Тверская",
        "phone": "89990000002",
        "date": "25.12.2025",
        "rent": "сутки",
        "colors": ["grey"]
    }
]


@pytest.mark.parametrize("user", data_sets)
@pytest.mark.parametrize("entry", ["top", "bottom"])
def test_scooter_order_full_flow(driver, user, entry):
    main = MainPage(driver)
    order = OrderPage(driver)
    final = FinalPage(driver)

    main.open()
    close_cookie_banner(driver)

    if entry == "top":
        main.click_top_order_button()
    else:
        main.click_bottom_order_button()

    order.enter_text(order.NAME, user["name"])
    order.enter_text(order.SURNAME, user["surname"])
    order.enter_text(order.ADDRESS, user["address"])
    order.select_metro(user["metro"])
    order.enter_text(order.PHONE, user["phone"])

    next_btn = order.wait.until(EC.element_to_be_clickable(order.NEXT_BUTTON))
    next_btn.click()

    order.enter_date(user["date"])
    order.select_rental_period(user["rent"])
    order.select_scooter_color(user["colors"])

    order.click_order_button()
    order.confirm_order()

    assert final.order_success_visible(), "Окно успешного оформления не появилось"

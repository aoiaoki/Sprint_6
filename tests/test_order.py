import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.final_page import FinalPage
from data.test_data import data_sets


@allure.title("Полный поток заказа самоката — проверка всех вариантов")
@pytest.mark.parametrize("user", data_sets)
@pytest.mark.parametrize("entry", ["top", "bottom"])
def test_scooter_order_full_flow(driver, user, entry):
    main = MainPage(driver)
    order = OrderPage(driver)
    final = FinalPage(driver)

    with allure.step("Открыть главную страницу"):
        main.open()
        main.close_cookie_banner()

    with allure.step(f"Нажать кнопку 'Заказать' ({entry})"):
        if entry == "top":
            main.click_top_order_button()
        else:
            main.click_bottom_order_button()

    with allure.step("Заполнить форму №1"):
        order.enter_text(order.NAME, user["name"])
        order.enter_text(order.SURNAME, user["surname"])
        order.enter_text(order.ADDRESS, user["address"])
        order.select_metro(user["metro"])
        order.enter_text(order.PHONE, user["phone"])
        order.click(order.NEXT_BUTTON)

    with allure.step("Заполнить форму №2"):
        order.enter_date(user["date"])
        order.select_rental_period(user["rent"])
        order.select_scooter_color(user["colors"])

    with allure.step("Подтвердить оформление заказа"):
        order.click_order_button()
        order.confirm_order()

    with allure.step("Проверить, что заказ оформлен"):
        assert final.order_success_visible(), "Окно успешного оформления не появилось"

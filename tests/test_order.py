import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.final_page import FinalPage
from data.test_data import data_sets


@allure.title("Полный поток заказа самоката")
class TestOrderFlow:

    @pytest.mark.parametrize("user", data_sets)
    @pytest.mark.parametrize("entry", ["top", "bottom"])
    def test_scooter_order_full_flow(self, driver, user, entry):
        main = MainPage(driver)
        order = OrderPage(driver)
        final = FinalPage(driver)

        main.open()
        main.close_cookie_banner()

        if entry == "top":
            main.click_top_order_button()
        else:
            main.click_bottom_order_button()

        order.enter_text(order.NAME, user["name"])
        order.enter_text(order.SURNAME, user["surname"])
        order.enter_text(order.ADDRESS, user["address"])
        order.select_metro(user["metro"])
        order.enter_text(order.PHONE, user["phone"])

        order.click(order.NEXT_BUTTON)

        order.enter_date(user["date"])
        order.select_rental_period(user["rent"])
        order.select_scooter_color(user["colors"])

        order.click_order_button()
        order.confirm_order()

        assert final.order_success_visible(), "Окно успешного оформления не появилось"


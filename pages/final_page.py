import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FinalPage(BasePage):
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @allure.step("Проверить отображение окна 'Заказ оформлен'")
    def order_success_visible(self) -> bool:
        try:
            elem = self.wait_for_visibility(self.SUCCESS_MODAL)
            return elem.is_displayed()
        except Exception:
            return False

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class FinalPage(BasePage):
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверить что окно 'Заказ оформлен' отображается")
    def order_success_visible(self) -> bool:
        try:
            return self.wait_for_visibility(self.SUCCESS_MODAL).is_displayed()
        except Exception:
            return False

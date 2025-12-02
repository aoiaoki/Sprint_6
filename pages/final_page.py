from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinalPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Модалка "Заказ оформлен"
        self.SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def order_success_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL)
        ).is_displayed()

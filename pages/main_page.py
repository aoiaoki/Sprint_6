from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    # Кнопка заказа сверху (первый совпавший Button_Button__ra12g)
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")

    # Кнопка заказа снизу
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm button")

    # FAQ
    FAQ_QUESTION = lambda self, i: (By.ID, f"accordion__heading-{i}")
    FAQ_ANSWER = lambda self, i: (By.ID, f"accordion__panel-{i}")

    # Логотипы
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # общий метод клика
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # открыть главную
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    # верхняя кнопка заказа
    def click_top_order_button(self):
        self.click(self.ORDER_BUTTON_TOP)

    # нижняя кнопка заказа
    def click_bottom_order_button(self):
        # 1️⃣ Скроллим до секции с кнопкой
        section = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "Home_FinishButton__1_cWm"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section)

        # 2️⃣ Ждём появления и кликабельности кнопки
        button = self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM)
        )

        # 3️⃣ Кликаем
        button.click()

    # открыть FAQ
    def open_faq_question(self, index):
        self.click(self.FAQ_QUESTION(index))

    # получить текст ответа FAQ
    def get_faq_answer_text(self, index):
        return self.wait.until(
            EC.visibility_of_element_located(self.FAQ_ANSWER(index))
        ).text

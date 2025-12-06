import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import QA_SCOOTER_BASE


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM_SECTION = (By.CLASS_NAME, "Home_FinishButton__1_cWm")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button")

    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    COOKIE_ACCEPT = (By.CSS_SELECTOR, ".App_CookieConsent__1yUIN button")

    FAQ_ROOT = (By.CLASS_NAME, "accordion")
    FAQ_QUESTION_TEMPLATE = "(//div[@class='accordion__button'])[{index}]"
    FAQ_ANSWER_TEMPLATE = "(//div[@class='accordion__panel'])[{index}]"

    @allure.step("Открыть главную страницу")
    def open(self):
        super().open(QA_SCOOTER_BASE)

    @allure.step("Закрыть cookie-баннер")
    def close_cookie_banner(self):
        try:
            self.click(self.COOKIE_ACCEPT)
        except Exception:
            pass

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_into_view(self.ORDER_BUTTON_BOTTOM_SECTION)
        self.click(self.ORDER_BUTTON_BOTTOM)

    def faq_question_locator(self, index: int):
        return (By.XPATH, self.FAQ_QUESTION_TEMPLATE.format(index=index + 1))

    def faq_answer_locator(self, index: int):
        return (By.XPATH, self.FAQ_ANSWER_TEMPLATE.format(index=index + 1))

    @allure.step("Открыть FAQ-вопрос №{index}")
    def open_faq_question(self, index: int):
        self.wait_for_visibility(self.FAQ_ROOT)
        question = self.faq_question_locator(index)
        self.scroll_into_view(question)
        self.js_click(question)

    @allure.step("Получить текст FAQ-ответа №{index}")
    def get_faq_answer_text(self, index: int) -> str:
        answer = self.faq_answer_locator(index)
        self.wait_for_visibility(answer)
        return self.get_text(answer)

    @allure.step("Клик по логотипу Scooter")
    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step("Клик по логотипу Yandex")
    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)


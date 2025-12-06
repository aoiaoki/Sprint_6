import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_DROPDOWN_OPTIONS = (By.CLASS_NAME, "Dropdown-option")

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[contains(normalize-space(), 'Заказать')]"
    )

    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")

    @allure.step("Ввести текст в поле {locator}")
    def enter_text(self, locator, text: str):
        self.send_keys(locator, text)

    @allure.step("Выбрать станцию метро: {station}")
    def select_metro(self, station: str):
        self.click(self.METRO_FIELD)
        self.send_keys(self.METRO_FIELD, station)
        option = (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station}']")
        self.click(option)

    @allure.step("Ввести дату доставки: {date}")
    def enter_date(self, date: str):
        self.click(self.DATE)
        self.send_keys(self.DATE, date)
        elem = self.wait_for_visibility(self.DATE)
        elem.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {rent}")
    def select_rental_period(self, rent: str):
        self.click(self.RENTAL_PERIOD)
        options = self.wait.until(lambda d: d.find_elements(*self.RENTAL_DROPDOWN_OPTIONS))
        for option in options:
            if option.text.strip() == rent:
                option.click()
                return
        raise AssertionError(f"Не найден срок аренды: '{rent}'")

    @allure.step("Выбрать цвет самоката: {colors}")
    def select_scooter_color(self, colors: list):
        for color in colors:
            locator = (By.CSS_SELECTOR, f"label[for='{color}']")
            self.click(locator)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.scroll_into_view(self.ORDER_BUTTON)
        self.js_click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_visibility(self.CONFIRM_YES)
        self.js_click(self.CONFIRM_YES)


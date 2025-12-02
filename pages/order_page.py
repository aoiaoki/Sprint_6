from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # --- Локаторы первой формы ---
        self.NAME = (By.XPATH, "//input[@placeholder='* Имя']")
        self.SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
        self.ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.METRO_FIELD = (By.CLASS_NAME, "select-search__input")
        self.PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

        # --- Локаторы второй формы ---
        self.DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
        self.RENTAL_DROPDOWN_OPTIONS = (By.CLASS_NAME, "Dropdown-option")

        # Чекбоксы для цветов
        # ID = black / grey
        # label for="black"
        # label for="grey"

        # ВАЖНО: единственная кнопка "Заказать" на второй форме
        self.ORDER_BUTTON = (
            By.XPATH,
            "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
        )

        # Кнопка "Да" в модалке подтверждения
        self.CONFIRM_YES = (By.XPATH, "//button[text()='Да']")


    def enter_text(self, locator, text):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(text)

    def select_metro(self, metro_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_FIELD))
        metro_input.send_keys(metro_name)

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='select-search__select']//div[text()='{metro_name}']")
            )
        )
        option.click()

    def enter_date(self, value):
        field = self.wait.until(EC.element_to_be_clickable(self.DATE))
        field.click()
        field.clear()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    def select_rental_period(self, period_text):
        rental = self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD))
        rental.click()

        options = self.wait.until(
            EC.visibility_of_all_elements_located(self.RENTAL_DROPDOWN_OPTIONS)
        )

        for option in options:
            if option.text.strip() == period_text:
                option.click()
                return
        raise Exception(f"Не найден срок аренды: {period_text}")

    def select_scooter_color(self, colors: list):
        for color in colors:
            label = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"label[for='{color}']"))
            )
            label.click()

    def click_order_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    def confirm_order(self):
        yes_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_YES))
        self.driver.execute_script("arguments[0].click();", yes_btn)

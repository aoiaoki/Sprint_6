import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть URL: {url}")
    def open(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_visibility(self, locator, timeout: int = None):
        if timeout:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout: int = None):
        if timeout:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, substring: str, timeout: int = None):
        if timeout:
            return WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))
        return self.wait.until(EC.url_contains(substring))

    def click(self, locator):
        elem = self.wait_for_clickable(locator)
        try:
            elem.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", elem)

    def send_keys(self, locator, text):
        elem = self.wait_for_visibility(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait_for_visibility(locator).text

    def scroll_into_view(self, locator):
        elem = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)

    def js_click(self, locator):
        elem = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].click();", elem)

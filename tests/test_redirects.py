import pytest
import allure
from pages.main_page import MainPage


@allure.title("Переход по логотипу скутера ведёт на домен qa-scooter")
class TestRedirects:
    def test_logo_scooter_redirect(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_logo_scooter()
        page.wait_for_url_contains("qa-scooter")
        assert "qa-scooter" in page.get_current_url()

    def test_logo_yandex_redirect(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_logo_yandex()

        # новая вкладка открывается в результате клика
        page.switch_to_last_tab()
        page.wait_for_url_contains("dzen", timeout=15)
        assert "dzen" in page.get_current_url().lower()

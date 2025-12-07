import allure
from pages.main_page import MainPage


@allure.title("Редирект по клику на логотип Scooter")
def test_logo_scooter_redirect(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open()
        page.close_cookie_banner()

    with allure.step("Кликнуть на логотип Scooter"):
        page.click_logo_scooter()

    with allure.step("Проверить, что остались на домене qa-scooter"):
        page.wait_for_url_contains("qa-scooter")
        assert "qa-scooter" in page.get_current_url(), \
            "Редирект по лого Scooter работает неверно"


@allure.title("Редирект по клику на логотип Yandex/Dzen")
def test_logo_yandex_redirect(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open()
        page.close_cookie_banner()

    with allure.step("Кликнуть на логотип Yandex"):
        page.click_logo_yandex()

    with allure.step("Переключиться на новую вкладку"):
        page.switch_to_last_tab()

    with allure.step("Проверить, что произошёл редирект на dzen"):
        page.wait_for_url_contains("dzen", timeout=15)
        assert "dzen" in page.get_current_url().lower(), \
            "Редирект по лого Yandex работает неверно"

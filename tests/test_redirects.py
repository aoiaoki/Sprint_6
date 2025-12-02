from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait


def test_logo_scooter_redirect(driver):
    page = MainPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/")

    page.click(page.LOGO_SCOOTER)

    WebDriverWait(driver, 5).until(
        lambda d: "qa-scooter" in d.current_url
    )

    assert "qa-scooter" in driver.current_url


def test_logo_yandex_redirect(driver):
    page = MainPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Кликаем логотип
    page.click(page.LOGO_YANDEX)

    # Переходим на новую вкладку
    driver.switch_to.window(driver.window_handles[-1])

    wait = WebDriverWait(driver, 15)

    # Ждём, пока новая вкладка перестанет быть about:blank
    wait.until(lambda d: d.current_url != "about:blank")

    # Ждём появления ключевого домена Дзена
    wait.until(lambda d: "dzen" in d.current_url.lower())

    assert "dzen" in driver.current_url.lower(), f"Открылось: {driver.current_url}"

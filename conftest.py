import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    # Firefox ≥ 120 уже содержит встроенный geckodriver → Service() можно вызвать без пути
    service = Service()

    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    options.set_preference("network.proxy.type", 0)  # защита от about:blank у редиректов

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


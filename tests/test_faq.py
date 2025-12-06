import pytest
import allure
from pages.main_page import MainPage


@allure.title("FAQ — ответы должны присутствовать и быть непустыми")
class TestFAQ:
    @pytest.mark.parametrize("index", range(8))
    def test_faq_answers(self, driver, index):
        page = MainPage(driver)
        page.open()
        page.close_cookie_banner()

        with allure.step(f"Открыть вопрос FAQ #{index}"):
            page.open_faq_question(index)

        with allure.step("Проверить, что ответ не пустой"):
            answer = page.get_faq_answer_text(index)
            assert answer.strip() != "", f"FAQ #{index} возвращает пустой ответ"

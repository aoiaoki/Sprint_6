import allure
import pytest
from pages.main_page import MainPage
from data.faq_answers import faq_expected


@allure.title("FAQ — ответы должны соответствовать эталонным текстам")
@pytest.mark.parametrize("index", range(len(faq_expected)))
def test_faq_answers(driver, index):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу и закрыть cookie-баннер"):
        page.open()
        page.close_cookie_banner()

    with allure.step(f"Открыть FAQ-вопрос №{index}"):
        page.open_faq_question(index)

    with allure.step(f"Проверить текст ответа FAQ №{index}"):
        actual_answer = page.get_faq_answer_text(index).strip()
        expected_answer = faq_expected[index]

        assert actual_answer == expected_answer, (
            f"FAQ #{index}: ожидается '{expected_answer}', "
            f"получено '{actual_answer}'"
        )

# Автоматизация тестирования сервиса «Самокат»
Проект автоматизации UI-тестов учебного веб-сервиса от Яндекса.

---

## 📌 Структура проекта
Sprint_6/
│
├──data
│ ├── faq_answers.py
│ └── test_data.py
│
├── pages/ # Page Object Model (POM)
│ ├── base_page.py
│ ├── main_page.py
│ ├── order_page.py
│ └── final_page.py
│
├── tests/ # Тесты
│ ├── test_faq.py
│ ├── test_order.py
│ └── test_redirects.py
│
├── urls.py
├── conftest.py
└── README.md 

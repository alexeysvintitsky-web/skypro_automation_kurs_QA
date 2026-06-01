"""
Тест для калькулятора с использованием Allure отчетов
"""
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Класс с тестами"""

    @allure.title("Проверка что 7 + 8 = 15 с задержкой 45 секунд")
    @allure.description("""
        Открываем калькулятор, ставим задержку 45 секунд,
        нажимаем 7 + 8 =, проверяем что получилось 15
    """)
    def test_calculator(self) -> None:
        """
        Главный тест. Тут все шаги по порядку
        """
        driver = webdriver.Chrome()

        try:
            with allure.step("Открыть страницу с калькулятором"):
                page = CalculatorPage(driver)
                page.open()

            with allure.step("Установить задержку 45 секунд"):
                page.set_delay("45")

            with allure.step("Нажать кнопку 7"):
                page.click_button("7")

            with allure.step("Нажать кнопку +"):
                page.click_button("+")

            with allure.step("Нажать кнопку 8"):
                page.click_button("8")

            with allure.step("Нажать кнопку ="):
                page.click_button("=")

            with allure.step("Подождать результат и получить его"):
                rezultat = page.get_result()

            with allure.step("Проверить что результат равен 15"):
                assert rezultat == "15", f"должно быть 15 а вышло {rezultat}"

        finally:
            with allure.step("Закрыть браузер"):
                driver.quit()
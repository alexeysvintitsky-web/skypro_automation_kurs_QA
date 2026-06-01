"""
Тут лежит класс для работы со страницей калькулятора
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """
    Этот класс помогает управлять калькулятором на странице
    """

    def __init__(self, driver):
        """
        Создает объект страницы

        Args:
            driver: веб-драйвер (хром, файрфокс и т.д.)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self) -> None:
        """
        Открывает страницу с калькулятором в браузере

        Returns:
            None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку перед тем как калькулятор посчитает

        Args:
            seconds: сколько секунд ждать (например "45")

        Returns:
            None
        """
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, value: str) -> None:
        """
        Нажимает на кнопку калькулятора

        Args:
            value: что написано на кнопке (7, +, 8, =)

        Returns:
            None
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self) -> str:
        """
        Ждет пока на экране появится 15 и возвращает результат

        Returns:
            str: текст который появился на экране (должно быть "15")
        """
        # тут тупо ждем пока на экране будет 15
        self.wait.until(lambda dr: dr.find_element(By.CLASS_NAME, "screen").text == "15")
        return self.driver.find_element(By.CLASS_NAME, "screen").text
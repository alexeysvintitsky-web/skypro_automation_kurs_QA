from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, value):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self):
        # тут тупо ждем пока на экране будет 15
        self.wait.until(lambda dr: dr.find_element(By.CLASS_NAME, "screen").text == "15")
        return self.driver.find_element(By.CLASS_NAME, "screen").text
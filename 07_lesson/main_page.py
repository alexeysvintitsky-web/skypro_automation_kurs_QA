from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_id):
        knopka = self.driver.find_element(By.ID, f"add-to-cart-{product_id}")
        knopka.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
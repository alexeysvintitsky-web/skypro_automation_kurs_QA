from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.presence_of_element_located((By.ID, "checkout")))

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Алексей")
    driver.find_element(By.ID, "last-name").send_keys("Свинтицкий")
    driver.find_element(By.ID, "postal-code").send_keys("101000")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    print(total_text)

    assert "58.29" in total_text

    driver.quit()
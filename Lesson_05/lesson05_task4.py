from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
knopka = driver.find_element(By.CLASS_NAME, "radius")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

knopka.click()

plashka = driver.find_element(By.CLASS_NAME, "success")
print(plashka.text)

driver.quit()
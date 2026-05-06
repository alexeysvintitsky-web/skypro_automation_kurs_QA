from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

time.sleep(10)

kartinki = driver.find_elements(By.TAG_NAME, "img")

src = kartinki[3].get_attribute("src")

print(src)

driver.quit()
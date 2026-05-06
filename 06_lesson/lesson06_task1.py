from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

knopka = driver.find_element(By.ID, "ajaxButton")
knopka.click()

#   код работает только при увеличении времени на 1 секунду
wait = WebDriverWait(driver, 16)
zelenaya_plashka = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))

text = zelenaya_plashka.text
print(text)

time.sleep(2)
driver.quit()
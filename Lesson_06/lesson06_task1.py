from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

time.sleep(20)

text = driver.find_element(By.CLASS_NAME, "bg-success").text
print(text)

driver.quit()
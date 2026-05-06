from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()

time.sleep(1)

noviy_text = driver.find_element(By.ID, "updatingButton").text
print(noviy_text)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()

WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

print(driver.find_element(By.ID, "updatingButton").text)

driver.quit()
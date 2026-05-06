from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "award")))
print(driver.find_element(By.ID, "award").get_attribute("src"))

driver.quit()
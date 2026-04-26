from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

pole = driver.find_element(By.TAG_NAME, "input")

pole.send_keys("12345")
pole.clear()
pole.send_keys("54321")

sleep(3)

driver.quit()
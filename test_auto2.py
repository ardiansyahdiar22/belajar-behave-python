from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demoqa.com/webtables')
driver.maximize_window()

for i in range(3):
    element_value = f"//span[@id='delete-record-{i+1}']"
    driver.find_element(By.XPATH, element_value).click()

time.sleep(3)


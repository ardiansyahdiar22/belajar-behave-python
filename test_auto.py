from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

input_uname = driver.find_element(By.ID, 'user-name')
input_uname.send_keys('standard_user')
input_psswd = driver.find_element(By.ID, 'password')
input_psswd.send_keys('secret_sauce')

driver.find_element(By.ID, 'login-button').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
time.sleep(2)
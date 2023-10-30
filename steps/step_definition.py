from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
import time


@given(u'User Open browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.maximize_window()

@when(u'Fill username')
def step_impl(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')

@when(u'Fill passoword')
def step_impl(context):
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when(u'User click login button')
def step_impl(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then(u'User direct to dashboard')
def step_impl(context):
    title_dashboard = context.driver.find_element(By.XPATH, "//*[@class='title']").text
    assert title_dashboard == 'Products'
    time.sleep(3)
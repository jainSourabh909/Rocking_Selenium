# Verify that the Dashboard is loaded - PyTest
# Create a Report to send to QA Lead - HTML --> Allure Report

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_01_idrive():
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.ID,"username")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.XPATH,"//input[@type='password' and @id='password']")
    password.send_keys("123456")

    submit_btn = driver.find_element(By.ID,"frm-btn")
    submit_btn.click()

    time.sleep(2)




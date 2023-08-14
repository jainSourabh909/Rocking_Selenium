import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
 pytest .\test_01_vwo_login.py -v -s --html=report.html

'''

def test_vwologin():
    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url
    driver.get("https://app.vwo.com")
    email_address_element=driver.find_element(By.ID,"login-username")
    email_address_element.send_keys("93npu2yyb0@esiix.com")

    password_element=driver.find_element(By.NAME,"password")
    password_element.send_keys("Wingify@123")

    sign_in_btn_element = driver.find_element(By.ID, "js-login-btn")
    sign_in_btn_element.click()

    # There is delay for 2-3 TO SIGN THATS WHY WE ADDED THE SLEEP
    time.sleep(5)
    Logger.info("title is--> " + driver.title)
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.get("https://sdet.live")
    driver.back()
    driver.forward()



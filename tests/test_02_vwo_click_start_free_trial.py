import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
pytest .\test_02_vwo_login.py -v -s --html=report.html

'''

def test_vwo_click_on_start_free_trial():
    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url
    driver.get("https://app.vwo.com")

    #### LINK_TEXT and PARTIAL_LINK_TEXT will only work in anchor tag <a></a>
    ###### click on text=Start a free trial,  by using LINK_TEXT
    link_text = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link_text.click()
    ###### click on text=Start a free trial,  by using PARTIAL_LINK_TEXT
    # partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    # partial_link_text.click()







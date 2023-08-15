import time
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''

'''

def test_awsome_qa_xpath_testing():
    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url

    driver.get("https://awesomeqa.com/xpath/")
    #### click on text=Make Appointment, by using link text
    mammal_animal = driver.find_element(By.XPATH, "//div[@class='Mammal']/h4").text
    print("\nprint mammal text-->",mammal_animal)

    print_animal_text = driver.find_element(By.XPATH, "//div[@class='Mammal']/ancestor::div/h2").text
    print("print animal text-->",print_animal_text)


    time.sleep(1)
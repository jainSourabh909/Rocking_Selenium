import time
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''
pytest .\test_03_katalon_appointment.py -v -s --html=report.html
'''

def test_negative_kataloon_apointment():
    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #### click on text=Make Appointment, by using link text
    link_text = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link_text.click()

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("John Doe")

    login = driver.find_element(By.CLASS_NAME, "btn-default")
    login.click()

    capture_error_mesz=driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    print("Error Message-->",capture_error_mesz)

    assert "Login failed!" in capture_error_mesz.text
    time.sleep(5)
    print("Execution Completed")

def test_positive_kataloon_apointment():
    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #### click on text=Make Appointment, by using link text
    link_text = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link_text.click()

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    login = driver.find_element(By.CLASS_NAME, "btn-default")
    login.click()

    select_facility_dropdown = Select(driver.find_element(By.ID,"combo_facility"))
    select_facility_dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
    time.sleep(1)

    driver.find_element(By.ID,"chk_hospotal_readmission").click()

    driver.find_element(By.NAME, "programs").click()

    txt_visit_date = driver.find_element(By.ID, "txt_visit_date")
    current_date = datetime.datetime.now()
    current_date_str=current_date.strftime("%d/%m/%Y")
    print("current_date_str:--> ", current_date_str)
    txt_visit_date.send_keys(current_date_str)

    txt_comment=driver.find_element(By.ID, "txt_comment")
    txt_comment.send_keys("I am Sourabh Jain.I have cold")

    driver.find_element(By.ID, "btn-book-appointment").click()

    time.sleep(5)
    h2Heading = driver.find_element(By.TAG_NAME,"h2")
    assert "Appointment Confirmation" in h2Heading.text
    print("Execution Completed")

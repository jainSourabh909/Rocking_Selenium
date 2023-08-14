import os.path
import time
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
'''
pytest .\test_03_katalon_appointment.py -v -s --html=report.html
'''

def test_kataloon_apointment():

    data_list = []
    data_dict = {}
    # dict=[{"UNIQUE_ID":1,"USERNAME":"John Doe","PASSWORD":"John Doe"},{"UNIQUE_ID":2,"USERNAME":"John Doe","PASSWORD":"ThisIsNotAPassword"}]
    # df=pd.DataFrame(dict)
    count_list = []
    count=0

    df = pd.read_excel('C:/Users/sourabh.jain/PycharmProjects/Rocking_Selenium/DATA/DATA.xlsx')

    for row in df.iterrows():
            count+=1
        # row_list.append(row["UNIQUE_ID"])
        # print("row_list",row_list)
            print(row["USERNAME"], row["PASSWORD"])
            Logger = logging.getLogger(__name__)
            #### create a session
            driver = webdriver.Chrome()
            ##### maximize the window
            driver.maximize_window()
            # #### navigate to url
            driver.get("https://katalon-demo-cura.herokuapp.com/")
            # #### click on text=Make Appointment, by using link text
            link_text = driver.find_element(By.LINK_TEXT, "Make Appointment")
            link_text.click()

            ## fill username
            username = driver.find_element(By.ID,"txt-username")
            username.send_keys(row["USERNAME"])
            ## fill password
            password = driver.find_element(By.NAME, "password")
            password.send_keys(row["PASSWORD"])
            ## clcik on login
            login = driver.find_element(By.CLASS_NAME, "btn-default")
            login.click()

            ## appylying try except to cater both testcase
            try:
                capture_error_mesz=driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
                print("Error Message-->",capture_error_mesz)
                assert "Login failed!" in capture_error_mesz.text
                ### saving error mesz in a variable
                action_mesz=capture_error_mesz.text

            except:
                select_facility_dropdown = Select(driver.find_element(By.ID, "combo_facility"))
                select_facility_dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
                time.sleep(1)

                driver.find_element(By.ID, "chk_hospotal_readmission").click()

                driver.find_element(By.NAME, "programs").click()

                txt_visit_date = driver.find_element(By.ID, "txt_visit_date")
                current_date = datetime.datetime.now()
                current_date_str = current_date.strftime("%d/%m/%Y")
                print("current_date_str:--> ", current_date_str)
                txt_visit_date.send_keys(current_date_str)

                txt_comment = driver.find_element(By.ID, "txt_comment")
                txt_comment.send_keys("I am Sourabh Jain.I have cold")

                driver.find_element(By.ID, "btn-book-appointment").click()

                time.sleep(5)
                h2Heading = driver.find_element(By.TAG_NAME, "h2")
                assert "Appointment Confirmation" in h2Heading.text
                ### saving successfull mesz in a variable
                action_mesz=h2Heading.text
            ### putting data in a dict
            data_dict["STATUS"] = action_mesz
            data_dict["USERNAME"] = row["USERNAME"]
            data_dict["PASSWORD"] = row["PASSWORD"]
            ### appending dict into list
            data_list.append(data_dict)
            time.sleep(2)
            print("data_list:::",data_list)
            #### converting dict into df
            df = pd.DataFrame(data_list)
            ##### converting df into csv
            file_name="data_status.csv"
            df.to_csv(file_name,mode="a",index=False,header=not os.path.isfile(file_name))
            ### stop the driver
            driver.quit()
            count_list.append(count)
    print("Number of records-->",len(count_list))
    print("Execution Completed")


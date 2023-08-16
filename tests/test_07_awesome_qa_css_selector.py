import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

'''

def test_awsome_qa_xpath_testing():

    Logger = logging.getLogger(__name__)
    #### create a session
    driver = webdriver.Chrome()
    ##### maximize the window
    driver.maximize_window()
    #### navigate to url

    driver.get("https://awesomeqa.com/css/")
    ### accessing class attribute using css selector
    class_first_attr = driver.find_element(By.CSS_SELECTOR,"div.first").get_attribute("class")
    print("\nClass First Attr-->",class_first_attr)

    ### using first child
    class_first_span_first = driver.find_element(By.CSS_SELECTOR,"div.first>span:first-child").text
    print("class first span first-->",class_first_span_first)

    ### using last child
    class_first_span_last = driver.find_element(By.CSS_SELECTOR, "div.first>span:last-child").text
    print("class first span last-->", class_first_span_last)

    ### using nth child
    class_first_span_three = driver.find_element(By.CSS_SELECTOR, "div.first>span:nth-child(3)").text
    print("class first span three-->", class_first_span_three)

    ### using nth child -- print odd child = 2n+1 ,we can use odd keyword also
    class_first_span_odd = driver.find_elements(By.CSS_SELECTOR, "div.first>span:nth-child(2n+1)")
    count=0
    for data in class_first_span_odd:
        count+=1
        print(f"class first span {count} odd-->", data.text)
    print("Total number of odd span-->",count)

    ### using nth child -- print even child = 2n
    class_first_span_even = driver.find_elements(By.CSS_SELECTOR, "div.first>span:nth-child(2n)")
    count = 0
    for data in class_first_span_even:
        count += 1
        print(f"class first span {count} even-->", data.text)
    print("Total number of even span-->", count)

    ### using nth child -- print even child = using even keyword
    class_first_span_even_keyword = driver.find_elements(By.CSS_SELECTOR, "div.first>span:nth-child(even)")
    count = 0
    for data in class_first_span_even_keyword:
        count += 1
        print(f"class first span {count} even-->", data.text)
    print("Total number of even span using even keyword-->", count)



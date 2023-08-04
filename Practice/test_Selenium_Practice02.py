import time
from selenium import webdriver
import pytest
from win32api import GetSystemMetrics
import wx

'''
if we wanna run all testcase--> pytest -v   ==(v=virbose)
if we wanna run pattern match testcase--> pytest -k "add" -v  ==(match_pattern = add)
if we wanna mark our test case--> @pytest.mark.positive  ==(mark_name=positive)
if we wanna run mark test case-->pytest -m "positive" -v -s (-s=print the output)
'''

@pytest.fixture
def driver_session():
    ## Create a Session
    print("\nStart")
    driver = webdriver.Chrome()
    ### before maximize wait for 2 sec
    time.sleep(2)
    ###### maximize window
    driver.maximize_window()
    ### after maximize wait for 5 sec
    time.sleep(5)
    return driver

def test_open_url_verify_title(driver_session):
    #### Navigation to url(Send the command)
    driver_session.get("https://app.vwo.com")
    print("Page_title-->",driver_session.title)
    ### getting system width and height using win32api lib under pypiwin32
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    ### setting window size to 600*500
    width = 600
    height = 500
    driver_session.set_window_size(width, height)
    ### adding sleep to see the small size
    time.sleep(2)
    ### using assertions
    # assert "Login - VWO"==driver_session.title
    # below is the another way to assert
    assert "Login - VWO" in driver_session.title

@pytest.mark.cxpython
def test_find_screen_size_through_wxpython():
    ## Create a Session
    print("\nStart")
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    ### adding sleep to see the small size
    time.sleep(1)
    # creating application object
    app1 = wx.App()
    screenxy = wx.GetDisplaySize()  # returns a tuple
    print("\nsystem_size-->",screenxy)
    driver.set_window_size(screenxy[0], screenxy[1])
    ### adding sleep to see the big size
    time.sleep(1)
    assert True
    # Close the driver
    driver.quit()
    print("End")
#
import time
from selenium import webdriver
import pytest
from win32api import GetSystemMetrics


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
    # Close the driver
    driver_session.quit()
    print("End")
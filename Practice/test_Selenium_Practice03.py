from selenium import  webdriver
import  logging


def test_login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")

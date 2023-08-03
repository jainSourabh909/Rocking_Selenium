import time
from selenium import webdriver


## Create a Session
print("Start")
driver = webdriver.Chrome()
### before maximize wait for 2 sec
time.sleep(2)
###### maximize window
driver.maximize_window()
### after maximize wait for 5 sec
time.sleep(5)
#### Navigation to url(Send the command)
driver.get("https://app.vwo.com")
print("End")
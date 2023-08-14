# Selenium Practice
### Commands Used 
1. Commands to install packages from requirements.txt file-->```pip install -r requirements.txt```
2. Commands to run Selenium_Practice01.py file code through terminal from main dir-->`py .\Practice\Selenium_Practice01.py`
2. Commands to run Selenium_Practice01.py file code through terminal from main dir-->`py .\Practice\Selenium_Practice01.py`
3. command to run test_Selenium_Practice02.py file code through terminal from main dir-->`pytest -v -s .\test_Selenium_Practice02.py`


##### Steps to Create a project
1. Create a virtual environment
2. Install required packages.
3. Create a folder Practice
4. Create a Selenium_Practice01.py file write some get url code.
5. Create a test_Selenium_Practice02.py file write some functions to get url.
6. install a package **pypiwin32** package to get system width and height.(`import-->from win32api import GetSystemMetrics`)


### Pytest Commands
1. if we want to run all testcase--> `pytest -v`   ==(v=virbose)
2. if we want to run pattern match testcase--> `pytest -k "add" -v`  ==(match_pattern = add)
3. if we want to mark our test case--> `@pytest.mark.positive`  ==(mark_name=positive)
4. if we want to run mark test case--> `pytest -m "positive" -v -s` (-s=print the output)

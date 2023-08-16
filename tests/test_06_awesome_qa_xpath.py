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

    driver.get("https://awesomeqa.com/xpath/")
    #### click on text=Make Appointment, by using link text
    mammal_animal = driver.find_element(By.XPATH, "//div[@class='Mammal']/h4").text
    print("\nprint mammal text-->",mammal_animal)

    ####### using ancestor keyword to find xpath
    print_animal_text = driver.find_element(By.XPATH, "//div[@class='Mammal']/ancestor::div/h2").text
    print("print animal text-->",print_animal_text)

    ####### using parent keyword to find xpath
    print_Vertebrate_text_xpath = driver.find_element(By.XPATH, "//div[@class='Mammal']/parent::div/h3").text
    print("print Vertebrate text-->", print_Vertebrate_text_xpath)

    ######### using contains fn
    print_Vertebrate_text_xpath_contains=driver.find_element(By.XPATH,"//h3[contains(text(), 'Vertebrate')]").text
    print("print Vertebrate text using xapth contains fn-->", print_Vertebrate_text_xpath_contains)

    print_words_starts_with_c_using_contains = driver.find_elements(By.XPATH, "//*[contains(text(), 'C')]")
    count = 0
    for data in print_words_starts_with_c_using_contains:
        count+=1
        print(f"Words that starts with 'C' using Contains {count} -->", data.text)

    ######### using starts-with fun
    print_words_starts_with_I_using_startswith =driver.find_elements(By.XPATH,"//*[starts-with(text(), 'I')]")
    count = 0
    for data in print_words_starts_with_I_using_startswith:
        count += 1
        print(f"Words that starts with 'I' using Startswith {count} -->", data.text)
    ##### using slash and dot " /../.. "  to find Parent xpath and / to find below element
    print_body_below_div_attr = driver.find_element(By.XPATH,"//div[@class='Mammal']/../../../div").get_attribute("align")
    print("Attribute of Div Tag - Align Below Body-->",print_body_below_div_attr)

    ####### using child keyword to find xpath
    print_first_child_of_mammal_class = driver.find_element(By.XPATH,"//div[@class='Mammal']/child::div[1]").get_attribute("class")
    print("Attribute(div) of First Child of Class-Mammal-->",print_first_child_of_mammal_class)

    print_first_child_of_mammal_class = driver.find_elements(By.XPATH,"//div[@class='Mammal']/child::div")
    count = 0
    for data in print_first_child_of_mammal_class:
        count += 1
        print(f"Attribute(div) of both Child of Class-Mammal div {count}-->", data.get_attribute("class"))

    print_second_child_of_mammal_class = driver.find_element(By.XPATH,"//div[@class='Mammal']/child::div[@class='Carnivore']/h5").text
    print("Heading of class Carnivore using mammal class -->",print_second_child_of_mammal_class)

    #### following-sibling in xpath
    find_all_siblings_of_fish = driver.find_elements(By.XPATH,"//div[@class='Fish']/following-sibling::div")
    count = 0
    for data in find_all_siblings_of_fish:
        count += 1
        print(f"All Siblings of Class Fish - {count}-->", data.get_attribute("class"))

    second_sibling_of_fish = driver.find_element(By.XPATH,"//div[@class='Fish']/following-sibling::div[2]").get_attribute("class")
    print("Attribute of Second Sibling(other) of Class Fish-->",second_sibling_of_fish)







    time.sleep(1)
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(2)
driver.find_element_by_link_text("REGISTER").click()
countryDropDown = Select(driver.find_element_by_name("country"))
countryDropDown.select_by_index(5)
time.sleep(2)
countryDropDown.select_by_value("15")
time.sleep(2)
countryDropDown.select_by_visible_text("GREENLAND")
time.sleep(2)
driver.quit()
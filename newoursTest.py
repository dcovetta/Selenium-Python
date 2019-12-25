import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class newtour(unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        time.sleep(2)

    def test_dropdown(self):
        self.driver.find_element_by_link_text("REGISTER").click()
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(5)
        countryDropDown.select_by_value("15")
        countryDropDown.select_by_visible_text("GREENLAND")
        self.assertEqual(countryDropDown.first_selected_option.text.strip(), "CONGO")

    def tearDown(self):
        self.driver.quit()


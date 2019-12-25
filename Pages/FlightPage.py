from selenium import webdriver
from selenium.webdriver.support.ui import Select

class FlightPage:
    def __init__(self, myDriver):
        self.driver = myDriver

    def select_country(self):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(5)
        countryDropDown.select_by_value("11")
        countryDropDown.select_by_visible_text("CONGO")

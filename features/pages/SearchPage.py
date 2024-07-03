from selenium.webdriver.common.by import By
from features.pages.BasePage import Base
from features.pages.locators import *

class Search(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_product(self):
        return self.display_status(*SearchPageLocators.VALID_PRODUCT)
    
    def display_status_of_message(self):
        return self.display_status(*SearchPageLocators.MESSAGE_VALIDATION)

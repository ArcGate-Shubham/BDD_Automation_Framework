from selenium.webdriver.common.by import By
from features.pages.BasePage import Base
from features.pages.locators import *

class Account(Base):
    def __init__(self, driver):
        self.driver = driver

    def display_status_of_edit_information_option(self):
        return self.display_status(*AsccountPageLocators.EDIT_ACCOUNT_INFORMATION_LINK_TEXT)

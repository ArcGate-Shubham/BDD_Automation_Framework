from selenium.webdriver.common.by import By
from features.pages.BasePage import Base
from features.pages.locators import *

class AccountSuccess(Base):
    
    def __init__(self, driver):
        self.driver = driver

    def display_status_of_account_created_heading(self):
        return self.display_status(*AccountSuccessPageLocators.ACCOUNT_SUCCESS_HEADING)

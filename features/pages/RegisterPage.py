from selenium.webdriver.common.by import By
from features.pages.AccountSuccessPage import AccountSuccess
from features.pages.BasePage import Base
from features.pages.locators import *

class Register(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        return self.type_into_element(first_name, *RegisterPageLocators.INPUT_FIRST_NAME)
    
    def enter_last_name(self, last_name):
        return self.type_into_element(last_name, *RegisterPageLocators.INPUT_LAST_NAME)
    
    def enter_email(self, email):
        return self.type_into_element(email, *RegisterPageLocators.INPUT_EMAIL)
    
    def enter_telephone(self, telephone):
        return self.type_into_element(telephone, *RegisterPageLocators.INPUT_TELEPHONE)
    
    def enter_password(self, password):
        return self.type_into_element(password, *RegisterPageLocators.INPUT_PASSWORD)
    
    def enter_confirm_password(self, confirm_password):
        return self.type_into_element(confirm_password, *RegisterPageLocators.INPUT_CONFIRM_PASSWORD)
    
    def select_privacy_policy(self):
        return self.click_on_element(*RegisterPageLocators.PRIVACY_POLICY)
        
    def click_on_continue_button(self):
        self.click_on_element(*RegisterPageLocators.CONTINUE_BUTTON)
        return AccountSuccess(self.driver)
    
    def select_yes_radio_button(self):
        self.click_on_element(*RegisterPageLocators.RADIO_BUTTON_YES_OPTION)
    
    def display_status_of_duplicate_email_warning(self, expected_text):
        return self.reterive_element_text_conatains(*RegisterPageLocators.DUPLICATE_EMAIL_WARNING, expected_text)

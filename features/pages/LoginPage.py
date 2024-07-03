from selenium.webdriver.common.by import By
from features.pages.AccountPage import Account
from features.pages.BasePage import Base
from features.pages.locators import *

class Login(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_address(self, email_text):
        return self.type_into_element(email_text, *LoginPageLocators.EMAIL_ADDRESS)

    def enter_password(self, password_text):
        return self.type_into_element(password_text, *LoginPageLocators.PASSWORD_FIELD)
        
    def click_on_login_button(self):
        self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)
        return Account(self.driver)
    
    def display_warning_message_of_status(self):
        return self.display_status(*LoginPageLocators.WARNING_MESSAGE)

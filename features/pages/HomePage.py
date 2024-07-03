from selenium.webdriver.common.by import By
from features.pages.BasePage import Base
from features.pages.LoginPage import Login
from features.pages.RegisterPage import Register
from features.pages.SearchPage import Search
from features.pages.locators import *

class Home(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_my_account(self):
        self.click_on_element(*HomePageLocators.MY_ACCOUNT_OPTION_BUTTON)

    def select_login_option(self):
        self.click_on_element(*HomePageLocators.LOGIN_OPTION_LINK_TEXT)
        return Login(self.driver)
    
    def check_home_page_title(self, expected_text):
        return self.verify_page_title(expected_text)
    
    def enter_product_info_search_box_field(self, product_text):
        return self.type_into_element(product_text, *HomePageLocators.SEARCH_BOX_FIELD)
    
    def click_on_search_button(self):
        self.click_on_element(*HomePageLocators.SEARCH_BUTTON)
        return Search(self.driver)
    
    def click_on_register_button(self):
        self.click_on_element(*HomePageLocators.REGISTER_BUTTON)
        return Register(self.driver)

from datetime import datetime
from behave import *

from features.pages.HomePage import Home
from features.pages.LoginPage import Login
from features.pages.AccountPage import Account
from utilities.EmailWithTimeStampGenerator import *

@given(u'I navigated to Login page')
def step_impl(self):
    self.home = Home(self.driver)
    self.home.click_on_my_account()
    self.login = self.home.select_login_option()

@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(self, email, password):
    self.login.enter_email_address(email)
    self.login.enter_password(password)

@when(u'I click on login button')
def step_impl(self):
    self.account = self.login.click_on_login_button()

@then(u'I should get logged in')
def step_impl(self):
    self.account.display_status_of_edit_information_option()

@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(self, password):
    invalid_email = get_new_email_with_timestamp()
    self.login.enter_email_address(invalid_email)
    self.login.enter_password(password)

@then(u'I should get a proper warning message')
def step_impl(self):
    assert self.login.display_warning_message_of_status()

@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(self, email, password):
    self.login.enter_email_address(email)
    self.login.enter_password(password)

@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(self, password):
    invalid_email = get_new_email_with_timestamp()
    self.login.enter_email_address(invalid_email)
    self.login.enter_password(password)

@when(u'I domt enter email and password into the fields')
def step_impl(self):
    self.login.enter_email_address('')
    self.login.enter_password('')

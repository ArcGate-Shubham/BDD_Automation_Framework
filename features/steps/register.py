from datetime import *
from behave import *

from features.pages.AccountSuccessPage import AccountSuccess
from features.pages.HomePage import Home
from features.pages.RegisterPage import Register
from utilities.EmailWithTimeStampGenerator import *


@given(u'I navigate to Register page')
def step_impl(self):
    self.home = Home(self.driver)
    self.home.click_on_my_account()
    self.register = self.home.click_on_register_button()

@when(u'I enter below details into mandatory fields')
def step_impl(self):
    for row in self.table:
        self.register.enter_first_name(row["first_name"])
        self.register.enter_last_name(row["last_name"])
        new_email = get_new_email_with_timestamp()
        self.register.enter_email(new_email)
        self.register.enter_telephone(row["telephone"])
        self.register.enter_password(row["password"])
        self.register.enter_confirm_password(row["password"])

@when(u'I select privacy policy option')
def step_impl(self):
    self.register.select_privacy_policy()

@when(u'I click on continue button')
def step_impl(self):
    self.account_success = self.register.click_on_continue_button()

@then(u'Account should get created')
def step_impl(self):
    assert self.account_success.display_status_of_account_created_heading()

@when(u'I enter below details into all fields')
def step_impl(self):
    for row in self.table:
        self.register.enter_first_name(row["first_name"])
        self.register.enter_last_name(row["last_name"])
        new_email = get_new_email_with_timestamp()
        self.register.enter_email(new_email)
        self.register.enter_telephone(row["telephone"])
        self.register.enter_password(row["password"])
        self.register.enter_confirm_password(row["password"])
        self.register.select_yes_radio_button()

@when(u'I enter details into all fields except email field')
def step_impl(self):
    for row in self.table:
        self.register.enter_first_name(row["first_name"])
        self.register.enter_last_name(row["last_name"])
        self.register.enter_telephone(row["telephone"])
        self.register.enter_password(row["password"])
        self.register.enter_confirm_password(row["password"])
        self.register.select_yes_radio_button()

@when(u'I enter existing accounts email into email field')
def step_impl(self):
    self.register.enter_email('amotooriapril20246@gmail.com')

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(self):
    self.register.display_status_of_duplicate_email_warning('Warning: E-Mail Address is already registered!')

@when(u'I dont enter anything into the fields')
def step_impl(self):
    self.register.enter_first_name('')
    self.register.enter_last_name('')
    self.register.enter_email('')
    self.register.enter_telephone('')
    self.register.enter_password('')
    self.register.enter_confirm_password('')

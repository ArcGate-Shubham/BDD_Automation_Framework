from behave import *

from features.pages.HomePage import Home
from features.pages.SearchPage import Search



@given(u'I got navigated to Home page')
def step_impl(self):
    self.home = Home(self.driver)
    assert self.home.check_home_page_title("Your Store")

@when(u'I enter valid product say "{product}" into the search box field')
def step_impl(self, product):
    self.home.enter_product_info_search_box_field(product)

@when(u'I click on search button')
def step_impl(self):
    self.search = self.home.click_on_search_button()

@then(u'valid product should get displayed in search results')
def step_impl(self):
    assert self.search.display_status_of_product()

@when(u'I enter invalid product say "{product}" into the search box field')
def step_impl(self, product):
    self.home.enter_product_info_search_box_field(product)

@then(u'Proper message should be displayed in search results')
def step_impl(self):
    assert self.search.display_status_of_message()

@when(u'I dont enter anything into the search box field')
def step_impl(self):
    self.home.enter_product_info_search_box_field('')
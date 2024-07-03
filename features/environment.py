import allure
from allure_commons.types import AttachmentType

from datetime import datetime
from selenium import webdriver
from utilities import ConfigReader


def before_scenario(self, driver):
    browser_name = ConfigReader.read_configuration("basic_info", "browser")
    if browser_name.__eq__("chrome"):
        self.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        self.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        self.driver = webdriver.Edge()
        
    self.driver.maximize_window()
    self.driver.get(ConfigReader.read_configuration("basic_info","url"))

def after_scenario(self, driver):
    self.driver.quit()

def after_step(self, step):
    if step.status == "failed":
        name = datetime.today().strftime('%Y-%m-%d-%M-%S') + "_send_keys_failure.png"
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

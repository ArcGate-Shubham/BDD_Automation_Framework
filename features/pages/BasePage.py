import allure
from allure_commons.types import AttachmentType
from datetime import datetime
from selenium.webdriver.common.by import By
from utilities.logger import *

class Base:

    log = LogClass.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            raise ValueError("Locator type '{}' is not supported.".format(locator_type))

    def click_on_element(self, locator="", locator_type="xpath", element=None):
        """
        Click on an element.
        Either provide element or a combination of locator and locator_type.
        """
        try:
            if locator:  
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        f"Locator not found. Cannot click on the element with locator: {locator}, locator_type: {locator_type}")
            element.click()
            self.log.info(f"Clicked on element with locator: {locator}, locator_type: {locator_type}")
        except AssertionError as e:
            self.log.error(e)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(f"{locator} not found")
            raise
        except Exception as ex:
            self.log.error(f"An error occurred while clicking on the element with locator: {locator}, locator_type: {locator_type}")
            self.log.error(ex)
            raise

    def get_element(self, locator, locator_type="xpath"):
        """
        Get element name
        locator: "It can be id, xpath, css_selector etc.."
        locator_type: by default its xpath.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element
    
    def verify_page_title(self, expected_text):
        return self.driver.title.__eq__(expected_text)

    def type_into_element(self, data, locator="", locator_type="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        "Locator not found. Cannot send data to the element with locator: {} "
                        "and locator_type: {}".format(locator, locator_type))
            element.click()
            element.clear()
            element.send_keys(data)
            self.log.info("Sent data '{}' to element with locator: {} and locator_type: {}".format(
                data, locator, locator_type))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S') + "_send_keys_failure.png"
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(locator + '_send_keys_failure')
            raise
        except Exception as e:
            self.log.exception("Failed to send data to the element with locator: {} and locator_type: {}. Error: {}".format(
                locator, locator_type, e))
            raise

    def display_status(self, locator="", locator_type="xpath", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_display = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_display = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locator_type: " + locator_type)
            else:
                self.log.error("Element not displayed with locator: " + locator + " locator_type: " + locator_type)
                
            return is_display
        except:
            print("Element not found")
            return False
        
    def reterive_element_text_conatains(self, locator, locator_type, expected_text):
        element = self.get_element(locator, locator_type)
        return element.text.__contains__(expected_text)

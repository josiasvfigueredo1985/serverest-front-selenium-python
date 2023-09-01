from driver_factory.driverfactory import driver
from selenium.webdriver.common.by import By


class interactions:
    def click_element(self, by: By, element):
        """
        The element click command is executed on the center of the element.
        If the center of the element is obscured for some reason, Selenium
        will return an element click intercepted error.
        """
        # Click on the element
        driver.find_element(by, element).click()

    def send_text(self, by: By, element, txt):
        """
        The element send keys command types the provided keys into an editable element.
        Typically, this means an element is an input element of a form with a text type
        or an element with a content-editable attribute. If it is not editable,
        an invalid element state error is returned.
        """
        # Enter Text
        driver.find_element(by, element).send_keys(txt)

    def clear_text(self, by: By, element):
        """
        The element clear command resets the content of an element.
        This requires an element to be editable, and resettable.
        Typically, this means an element is an input element of a
        form with a text type or an element with a content-editable attribute.
        If these conditions are not met, an invalid element state error is returned.
        """
        # Clear field to empty it from any previous data
        driver.find_element(by, element).clear()

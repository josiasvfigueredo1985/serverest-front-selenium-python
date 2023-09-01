from driver_factory.driverfactory import driver
from selenium.webdriver.common.by import By


class information:
    def return_is_displayed(self, by: By, element):
        """
        This method is used to check if the connected Element is displayed on a webpage.
        Returns a Boolean value, True if the connected element is displayed in the
        current browsing context else returns false.

        This functionality is mentioned in, but not defined by the w3c specification
        due to the impossibility of covering all potential conditions.
        As such, Selenium cannot expect drivers to implement this functionality directly,
        and now relies on executing a large JavaScript function directly.
        This function makes many approximations about an element's nature and relationship
        in the tree to return a value.
        """
        displayed = driver.find_element(by, element).is_displayed()
        return displayed

    def return_is_enabled(self, by: By, element):
        """
        This method is used to check if the connected Element is enabled or disabled
        on a webpage. Returns a boolean value, True if the connected element is enabled
        in the current browsing context else returns false.
        """
        enabled = driver.find_element(by, element).is_enabled()
        return enabled

    def return_is_selected(self, by: By, element):
        """
        This method determines if the referenced Element is Selected or not.
        This method is widely used on Check boxes, radio buttons, input elements,
        and option elements.

        Returns a boolean value, True if referenced element is selected
        in the current browsing context else returns false.
        """
        selected = driver.find_element(by, element).is_selected()
        return selected

    def return_tag_name(self, by: By, element):
        """
        It is used to fetch the TagName of the referenced Element which has the focus
        in the current browsing context.
        """
        # Returns TagName of the element
        tag = driver.find_element(by, element).tag_name
        return tag

    def return_size_position(self, by: By, element):
        """
        It is used to fetch the dimensions and coordinates of the referenced element.

        The fetched data body contain the following details:

        X-axis position from the top-left corner of the element
        y-axis position from the top-left corner of the element
        Height of the element
        Width of the element
        """
        res = driver.find_element(by, element).rect
        return res

    def return_css_value(self, by: By, element, css_property):
        """
        Retrieves the value of specified computed style property of an element in the
        current browsing context.
        Example:
        # Navigate to Url
        driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

        # Retrieves the computed style property 'color' of link text
        cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')
        """
        cssValue = driver.find_element(by, element).value_of_css_property(css_property)
        return cssValue

    def return_text_content(self, by: By, element):
        """
        Retrieves the rendered text of the specified element.
        """
        # Retrieves the text of the element
        txt = driver.find_element(by, element).text
        return txt

    def return_attributes_properties(self, by: By, element, attribute):
        """
        Fetches the run time value associated with a DOM attribute.
        It returns the data associated with the DOM attribute or property of the element.
        """
        # Identify the email text box
        dom_element = driver.find_element(by, element)
        # Fetch the value property associated with the textbox
        data = dom_element.get_attribute(attribute)
        return data

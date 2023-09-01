from driver_factory.driverfactory import driver, By


class finders:
    def get_single_element(self, by: By, element):
        """Recommended to use when a single element must to be returned,
        To improve the performance slightly, we can use either CSS or
        XPath to find this element in a single command."""
        single_element = driver.find_element(by, element)
        return single_element

    def get_multiple_elements(self, by: By, element):
        """Recommended to use when a multiple element must be returned,
        for lists is recommended to use tag_name, in order to fetch data
        from all elements that match with the tag name
        There are several use cases for needing to get references to all
        elements that match a locator, rather than just the first one.
        The plural find elements methods return a collection of element references.
        If there are no matches, an empty list is returned.

        Often you get a collection of elements but want to work with a specific element,
        which means you need to iterate over the collection and identify the one you want.
        """
        multiple_elements = driver.find_elements(by, element)
        return multiple_elements

    """Find Elements From Element
    It is used to find the list of matching child WebElements within the context of 
    parent element. To achieve this, the parent WebElement is chained with 'findElements' 
    to access child elements

    Example:
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

        # Get element with tag name 'div'
    element = driver.find_element(By.TAG_NAME, 'div')

        # Get all the elements available with tag name 'p'
    elements = element.find_elements(By.TAG_NAME, 'p')
    for e in elements:
        print(e.text)
    """

    def get_active_element(self, by: By, element, attribute):
        """
        It is used to track (or) find DOM element which has the focus in the current browsing
        context.
        """
        driver.find_element(by, element)
        # Get attribute of current active element
        attr = driver.switch_to.active_element.get_attribute(attribute)
        return attr

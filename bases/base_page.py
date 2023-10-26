"""Base Page module for pages implementing"""

from xml.dom import NotFoundErr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """# Base Page class
    - Implements all necessary methods to create a new page or steps
    - This class waits for a WebDriver instance type
    - As long it's a instance from WebDriver, the driver don't matter
    - It could be any of WebDriver instance, like Firefox or Edge
    """

    base_url = "https://www.selenium.dev/selenium/web"
    by = By

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 20

    def open_base_url(self, prefix_url=base_url):
        """Open the base URL"""
        self.driver.get(self.base_url + prefix_url)

    def take_screenshot_error(self, locator):
        """Take a screenshot when some error occurs"""
        self.driver.save_screenshot(f"element_{locator}_on_{self.driver.title}.png")

    def wait_element_be_displayed(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            visible = self.driver.find_element(by, locator)
            element = wait.until(lambda d: visible.is_displayed())
            return element
        except NotFoundErr(f"Element {element} not displayed!") as nde:
            self.take_screenshot_error(locator)
            return nde

    def wait_element_be_present(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except NotFoundErr(f"Element {element} not present") as npe:
            self.take_screenshot_error(locator)
            return npe

    def click(self, by: By, locator):
        """Click a element"""
        self.wait_element_be_displayed(by, locator)
        self.driver.find_element(by, locator).click()

    def write(self, by: By, locator, text):
        """Write text to input field"""
        self.wait_element_be_displayed(by, locator)
        self.driver.find_element(by, locator).send_keys(text)

    def clear(self, by: By, locator):
        """Clear input field"""
        self.wait_element_be_displayed(by, locator)
        self.driver.find_element(by, locator).clear()

    def upload_file(self, by: By, locator, filename):
        """Uploads a file
        - Filename must be provided as full path"""
        self.wait_element_be_displayed(by, locator)
        self.driver.find_element(by, locator).send_keys(filename)
        self.driver.find_element(by, locator).submit()
        if any(
            keyword in self.driver.page_source
            for keyword in ["File Uploaded", "Uploaded", "Upload"]
        ):
            print("file upload success")
        else:
            print("file upload not successful")

    def get_element_text(self, by: By, locator) -> str:
        """Get the element text"""
        self.wait_element_be_displayed(by, locator)
        el_text = self.driver.find_element(by, locator).text
        return el_text

    def get_page_title(self) -> str:
        """Get the page title"""
        return self.driver.title

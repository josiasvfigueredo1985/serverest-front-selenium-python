"""Base Page module for pages implementing"""

from faulthandler import is_enabled

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bases.base_test import TestBase
from utils.general import general

exception = selenium.common.exceptions


class BasePage:
    """# Base Page class
    - Implements all necessary methods to create a new page or steps
    - All methods are generic and can be used for any class that inherits from BasePage class
    - This class waits for a WebDriver instance type
    - As long it's a instance from WebDriver, the driver don't matter
    - It could be any of WebDriver instance, like Firefox or Edge
    """

    base_url = "https://www.selenium.dev/selenium/web"
    by = By
    root_directory = general.root_dir
    report_folder = TestBase().reports_folder
    count: int = 1

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 20

    def open_base_url(self, prefix_url=base_url):
        """Open the base URL"""
        self.driver.get(self.base_url + prefix_url)

    def take_screenshot_error(self, locator):
        """Take a screenshot when some error occurs"""
        file_name = f"element_{self.count}_{locator}_on_{self.driver.title}.png"
        file_path: str = f"{self.root_directory}/{self.report_folder}/{file_name}"
        self.driver.save_screenshot(file_path)
        self.count += 1

    def wait_element_be_visible(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            visible = self.driver.find_element(by, locator)
            element = wait.until(lambda d: visible.is_displayed())
            return element
        except exception.ElementNotVisibleException(
            f"Element {element} not visible!"
        ) as nve:
            self.take_screenshot_error(locator)
            return nve

    def wait_element_be_present(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except exception.NoSuchElementException(
            f"Element {element} not present!"
        ) as npe:
            self.take_screenshot_error(locator)
            return npe

    def wait_element_be_enabled(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_located_selection_state_to_be((by, locator), is_enabled())
            )
            return element
        except exception.ElementNotInteractableException(
            f"Element {element} not enabled!"
        ) as nee:
            self.take_screenshot_error(locator)
            return nee

    def wait_element_be_clickable(self, by: By, locator):
        """Wait for and return the element(s) selected by css_selector."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            return element
        except exception.ElementNotVisibleException(
            f"Element {element} not clickable!"
        ) as nce:
            self.take_screenshot_error(locator)
            return nce

    def check_enabled_element(self, by: By, locator) -> bool:
        """Check if the element is enabled"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_located_selection_state_to_be((by, locator), is_enabled())
        )

    def check_invisible_element(self, by: By, locator) -> bool:
        """Check if the element is invisible or not present"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located((by, locator))
        )

    def check_visible_element(self, by: By, locator) -> bool:
        """Check if the element is invisible or not present"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def click(self, by: By, locator):
        """Click a element"""
        self.wait_element_be_clickable(by, locator)
        self.driver.find_element(by, locator).click()

    def write(self, by: By, locator, text):
        """Write text to input field"""
        self.wait_element_be_visible(by, locator)
        self.driver.find_element(by, locator).send_keys(text)

    def clear(self, by: By, locator):
        """Clear input field"""
        self.wait_element_be_visible(by, locator)
        self.driver.find_element(by, locator).clear()

    def upload_file(self, by: By, locator, filename):
        """Uploads a file
        - Filename must be provided as full path"""
        self.wait_element_be_visible(by, locator)
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
        self.wait_element_be_visible(by, locator)
        el_text = self.driver.find_element(by, locator).text
        return el_text

    def get_page_title(self) -> str:
        """Get the page title"""
        return self.driver.title

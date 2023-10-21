from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import Driver


class BasePage:
    utils = Driver()
    driver = utils.get_driver()
    timeout = 20

    def wait_element_be_visible(self, locator):
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def click(self, by: By, locator):
        self.wait_element_be_visible(locator)
        self.driver.find_element(by, locator).click()

    def write(self, by: By, locator, text):
        self.wait_element_be_visible(locator)
        self.driver.find_element(by, locator).send_keys(text)

    def clear(self, by: By, locator):
        self.wait_element_be_visible(locator)
        self.driver.find_element(by, locator).clear()

    def upload_file(self, by: By, locator, filename):
        self.wait_element_be_visible(locator)
        self.driver.find_element(by, locator).send_keys(filename)
        self.driver.find_element(by, locator).submit()
        if any(
            keyword in self.driver.page_source
            for keyword in ["File Uploaded", "Uploaded", "Upload"]
        ):
            print("file upload success")
        else:
            print("file upload not successful")

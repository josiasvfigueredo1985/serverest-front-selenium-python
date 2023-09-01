from driver_factory.driverfactory import driver, By
from selenium.webdriver.support.wait import WebDriverWait
import time


class waits:
    ####################################   WAITS  ##################################
    ###### Explicit Wait ######
    ### Displayed ####
    # Function to accepts any locator strategy
    def exp_wait_displayed_by(self, by: By, locator):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_by = driver.find_element(by, locator)
        wait.until(lambda d: exp_wait_by.is_displayed)

    # Use example:
    # self.exp_wait_displayed_by(By.XPATH,'//*[@id="example"]')

    def exp_wait_displayed_by_class_name(self, class_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CLASS_NAME, class_name)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_css_selector(self, css_selector):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CSS_SELECTOR, css_selector)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_id(self, id):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.ID, id)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_name(self, name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.NAME, name)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_link_text(self, link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.LINK_TEXT, link_text)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_partial_link_text(self, partial_link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_tag_name(self, tag_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.TAG_NAME, tag_name)
        wait.until(lambda d: exp_wait_class.is_displayed)

    def exp_wait_displayed_by_xpath(self, xpath):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.XPATH, xpath)
        wait.until(lambda d: exp_wait_class.is_displayed)

    ### Enabled ####
    # Function to accepts any locator strategy
    def exp_wait_enabled_by(self, by: By, locator):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_by = driver.find_element(by, locator)
        wait.until(lambda d: exp_wait_by.is_enabled)

    # Use example:
    # self.exp_wait_enabled_by(By.XPATH,'//*[@id="example"]')
    def exp_wait_enabled_by_class_name(self, class_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CLASS_NAME, class_name)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_css_selector(self, css_selector):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CSS_SELECTOR, css_selector)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_id(self, id):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.ID, id)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_name(self, name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.NAME, name)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_link_text(self, link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.LINK_TEXT, link_text)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_partial_link_text(self, partial_link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_tag_name(self, tag_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.TAG_NAME, tag_name)
        wait.until(lambda d: exp_wait_class.is_enabled)

    def exp_wait_enabled_by_xpath(self, xpath):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.XPATH, xpath)
        wait.until(lambda d: exp_wait_class.is_enabled)

    ### Selected ####
    # Function to accepts any locator strategy
    def exp_wait_selected_by(self, by: By, locator):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_by = driver.find_element(by, locator)
        wait.until(lambda d: exp_wait_by.is_selected)

    # Use example:
    # self.exp_wait_selected_by(By.XPATH,'//*[@id="example"]')
    def exp_wait_selected_by_class_name(self, class_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CLASS_NAME, class_name)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_css_selector(self, css_selector):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.CSS_SELECTOR, css_selector)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_id(self, id):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.ID, id)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_name(self, name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.NAME, name)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_link_text(self, link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.LINK_TEXT, link_text)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_partial_link_text(self, partial_link_text):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_tag_name(self, tag_name):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.TAG_NAME, tag_name)
        wait.until(lambda d: exp_wait_class.is_selected)

    def exp_wait_selected_by_xpath(self, xpath):
        wait = WebDriverWait(driver, timeout=2)
        exp_wait_class = driver.find_element(By.XPATH, xpath)
        wait.until(lambda d: exp_wait_class.is_selected)

    ###### Implicit Wait ######
    def imp_wait(self, wait_time: float):
        driver.implicitly_wait(wait_time)

    ###### Sleep ######
    def sleep_wait(self, wait_time: float):
        time.sleep(wait_time)

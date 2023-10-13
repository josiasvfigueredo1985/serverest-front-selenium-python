from selenium.webdriver.common.by import By

from utilities.driver_utils import DriverUtils


class BasePage(DriverUtils):
    def __init__(self):
        self.by = By
        self.instance = self.get_driver()
        super(BasePage, self.instance).__init__()

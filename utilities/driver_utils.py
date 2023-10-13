from selenium import webdriver


class DriverUtils:
    driver = None

    def create_driver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def get_driver(self):
        if self.driver is None:
            self.create_driver()
        return self.driver

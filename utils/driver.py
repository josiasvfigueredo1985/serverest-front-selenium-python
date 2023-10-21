from os import stat
from selenium import webdriver


class Driver:
    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        headless = False

        if headless:
            chrome_options.add_argument("--headless")
        if chrome_options:
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = webdriver.Chrome()

    def get_driver(self):
        if self.driver is None:
            self.create_driver()
        return self.driver

    def kill_driver(self):
        if self.diver is not None:
            self.driver.close()
            self.driver.quit()

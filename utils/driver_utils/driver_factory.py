from selenium import webdriver


class DriverFactory:
    def __init__(self):
        self.__create_driver()
        self.driver = self.__get_driver()

    def __create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        headless = False
        if headless:
            chrome_options.add_argument("--headless")
        if chrome_options:
            self._driver = webdriver.Chrome(options=chrome_options)
        else:
            self._driver = webdriver.Chrome()

    def __get_driver(self):
        return self._driver

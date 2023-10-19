from selenium import webdriver
import selenium


# Always follow the nomenclature policy for Pytest, the keyword is Test before any class or test case as such below:
class Driver:
    def create_driver(self):
        options = webdriver.ChromeOptions()
        headless = False
        if headless:
            options.add_argument("--headless")
        if options:
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Chrome()


    def get_driver(self):
        return self.driver
"""Driver Factory Module"""
from selenium import webdriver


class DriverFactory:
    """# Driver Factory for Selenium WebDriver
    - Singleton instance
    - Can create instance for specific driver such as Chrome or Firefox
    """

    instance = None
    driver = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(DriverFactory, cls).__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def __init__(self):
        if self.driver is None:
            self.create_driver()

    def create_driver(self):
        """Create driver method
        - Single responsibility principle to create driver instance"""
        self.driver = webdriver

    def get_driver(self):
        """Get driver method
        - Single responsibility principle to get driver instance"""
        return self.driver.Chrome()

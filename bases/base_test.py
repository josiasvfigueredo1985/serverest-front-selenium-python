"""Test Base class"""
from utils.driver_utils.driver_factory import DriverFactory


class TestBase:
    """# Test Base class
    - Organize the test execution for all the test class that inherit from this class"""

    driver = None

    def setup(self):
        """Setup method to instance driver from Driver Factory"""
        browser = DriverFactory()
        self.driver = browser.get_driver()

    def teardown(self):
        """Teardown method to close and quit the driver"""
        self.driver.close()
        self.driver.quit()

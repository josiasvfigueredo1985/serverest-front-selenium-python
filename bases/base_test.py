"""Test Base class"""
from utils.driver_utils.driver_factory import DriverFactory
from utils.general import general


class TestBase:
    """# Test Base class
    - Organize the test execution for all the test class that inherit from this class"""

    driver = None
    general = general
    reports_folder = "./reports/not_found_errors"

    def setup(self):
        """Setup method to instance driver from Driver Factory"""
        browser = DriverFactory()
        self.driver = browser.get_driver()
        self.remove_not_found_errors_folder()
        self.create_not_founnd_errors_folder()

    def create_not_founnd_errors_folder(self):
        """Create folders for reports and screenshots"""
        self.general.create_directory(self.reports_folder)

    def remove_not_found_errors_folder(self):
        """Remove errors screenshots folder"""
        self.general.remove_directory(self.reports_folder)

    def teardown(self):
        """Teardown method to close and quit the driver"""
        self.driver.close()
        self.driver.quit()

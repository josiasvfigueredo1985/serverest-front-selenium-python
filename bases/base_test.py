"""Test Base class"""
from utils.driver_utils.driver_factory import DriverFactory
from utils.general import general


class TestBase:
    """# Test Base class
    - Organize the test execution for all the test class that inherit from this class"""

    driver = None
    general = general
    reports_folder = "reports/"
    not_found_errors_folder = "not_found_errors/"
    html_report_folder = "html_report/"

    def setup(self):
        """Setup method to instance driver from Driver Factory"""
        browser = DriverFactory()
        self.driver = browser.get_driver()
        self.remove_test_report_folders()
        self.create_test_report_folders()

    def create_test_report_folders(self):
        """Create folders for reports and screenshots"""
        self.general.create_directory(
            self.reports_folder + self.not_found_errors_folder
        )
        self.general.create_directory(self.reports_folder + self.html_report_folder)

    def remove_test_report_folders(self):
        """Remove reports_folder and its child folders and content"""
        self.general.remove_directory(self.reports_folder)

    def teardown(self):
        """Teardown method to close and quit the driver"""
        self.driver.close()
        self.driver.quit()

from utils.driver_factory import DriverFactory


class TestBase:
    def setup(self):
        self.driver = DriverFactory().driver

    def teardown(self):
        self.driver.close()
        self.driver.quit()

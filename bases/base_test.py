from utils.driver_utils.driver_factory import DriverFactory


class TestBase:
    def setup(self):
        self.driver = DriverFactory()

    def teardown(self):
        self.driver.driver.close()
        self.driver.driver.quit()

from utilities.driver_utils import DriverUtils
import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = DriverUtils.create_driver(self)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

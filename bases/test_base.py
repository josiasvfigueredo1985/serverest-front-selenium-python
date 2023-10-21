from utils.driver import Driver


class TestBase:
    utils = Driver()

    def open(self):
        self.driver = self.utils.get_driver()
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    def setup(self):
        self.open()

    def teardown(self):
        self.utils.kill_driver()

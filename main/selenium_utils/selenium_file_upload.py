from driver_factory.driverfactory import driver, By


class file_upload:
    def file_upload(self, by: By, locator, file_name):
        driver.find_element(by, locator).send_keys(file_name)

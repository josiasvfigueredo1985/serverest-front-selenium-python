from driver_factory.driverfactory import By, driver
from selenium_utils.selenium_waits import waits
from selenium_utils.selenium_file_upload import file_upload
from selenium_utils.selenium_finders import finders
from selenium_utils.selenium_information import information
from selenium_utils.selenium_interactions import interactions


class utils(waits, file_upload, finders, information, interactions):
    Close = driver.quit()
    By = By()
    waits = waits()
    fileupload = file_upload()
    finders = finders()
    info = information()
    interactions = interactions()

from driver_factory.driverfactory import driver, By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_waits import waits
from selenium_file_upload import file_upload
from selenium_finders import finders
from selenium_information import information
from selenium_interactions import interactions


class utils(waits, file_upload, finders, information, interactions):
    waits = waits()
    fileupload = file_upload()
    finders = finders()
    info = information()
    interactions = interactions()

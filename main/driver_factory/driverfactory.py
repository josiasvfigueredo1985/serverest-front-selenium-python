from selenium import webdriver
from selenium.webdriver.common.by import By

By = By
driver = webdriver.Chrome()
driver.get("https://www.metal-archives.com/")
driver.implicitly_wait(0.5)
driver.maximize_window()

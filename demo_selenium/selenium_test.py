import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSeleniumForm:
    """Demo test for Selenium Form"""

    @pytest.mark.parametrize("search_term", ["Selenium", "Python", "PyTest"])
    def test_selenium_form(self, search_term):
        """Parametrization using decorators"""
        options = webdriver.ChromeOptions()
        headless = False
        if headless:
            options.add_argument("--headless")
        if options:
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title
        assert title == "Web form"
        driver.implicitly_wait(5)  # Implicitly wait for elements
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys(search_term)
        time.sleep(1)  # sleep for x seconds without Selenium interaction
        submit_button.click()
        message = driver.find_element(by=By.ID, value="message")
        text = message.text
        assert text == "Received!"

        driver.quit()

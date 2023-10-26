import time

import pytest
from selenium.webdriver.common.by import By

from bases.base_test import TestBase
from steps.web_form_steps import WebFormSteps


class TestSeleniumWebForm(TestBase):
    """Demo test for Selenium Web Form"""

    @pytest.mark.parametrize("search_term", ["Selenium", "Python", "PyTest"])
    def test_selenium_form(self, search_term):
        """Parametrization using decorators"""
        driver = self.driver.driver
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        title = driver.title
        assert title == "Web form"
        driver.implicitly_wait(5)
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys(search_term)
        time.sleep(1)
        submit_button.click()
        message = driver.find_element(by=By.ID, value="message")
        text = message.text
        assert text == "Received!"

    @pytest.mark.parametrize("search_term", ["Selenium", "Python", "PyTest"])
    def test_selenium_web_form(self, search_term):
        """Parametrization using decorators
        - Test adjusted using POM"""
        form = WebFormSteps(self.driver)
        form.openWebFormPage()
        title = form.getWebFormTitle()
        assert title == "Web form"
        form.submitTextIntoTextInputField(search_term)
        assert form.getFormSubmittedMessage() == "Received!"

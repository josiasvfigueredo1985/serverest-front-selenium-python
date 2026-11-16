"""Selenium Web Form Tests"""
from unittest.mock import MagicMock, PropertyMock

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from bases.base_test import TestBase
from steps.web_form_steps import WebFormSteps


def wait_for_web_form(driver):
    """Wait for the form and its title before checking the page."""
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))
    wait.until(EC.title_is("Web form"))


def test_wait_for_web_form():
    driver = MagicMock()
    driver.find_element.return_value.is_displayed.side_effect = [False, True]
    title = PropertyMock(side_effect=["", "Web form"])
    type(driver).title = title

    wait_for_web_form(driver)

    assert driver.find_element.call_count == 2
    assert title.call_count == 2


class TestSeleniumWebForm(TestBase):
    """Demo test for Selenium Web Form"""

    @pytest.mark.parametrize("search_term", ["Selenium", "Python", "PyTest"])
    def test_selenium_form(self, search_term):
        """Parametrization using decorators"""
        driver = self.driver
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        wait_for_web_form(driver)
        title = driver.title
        assert title == "Web form"
        wait = WebDriverWait(driver, 20)
        text_box = wait.until(EC.element_to_be_clickable((By.NAME, "my-text")))
        text_box.send_keys(search_term)
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        submit_button.click()
        message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
        text = message.text
        assert text == "Received!"

    @pytest.mark.parametrize("search_term", ["Selenium", "Python", "PyTest"])
    def test_selenium_web_form(self, search_term):
        """Parametrization using decorators
        - Test adjusted using POM"""
        form = WebFormSteps(self.driver)
        form.open_web_form_page()
        wait_for_web_form(self.driver)
        title = form.get_web_form_title()
        assert title == "Web form"
        form.submit_text_into_text_input_field(search_term)
        assert form.get_form_submitted_message() == "Received!"

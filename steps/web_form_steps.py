"""Web Form Steps"""
from pages.web_form_page import WebFormPage


class WebFormSteps(WebFormPage):
    """Web Form Steps"""

    def submit_text_into_text_input_field(self, text_input: str):
        """Web Form Steps"""
        self.text_input_field(text_input)
        self.click_submit_button()

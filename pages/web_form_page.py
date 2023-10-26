"""Web Form page"""
from bases.base_page import BasePage


class WebFormPage(BasePage):
    """Web Form page attributes and methods"""

    text_input = "my-text-id"
    submit_button = "button"
    message = "message"
    prefix_url = "/web-form.html"

    def open_web_form_page(self):
        """Open Web Form page calling the open_base_url method
        - Page prefix is passed as argument"""
        self.open_base_url(self.prefix_url)

    def text_input_field(self, input_string):
        """Text input field"""
        self.write(self.by.ID, self.text_input, input_string)

    def click_submit_button(self):
        """Click Submit button"""
        self.click(self.by.CSS_SELECTOR, self.submit_button)

    def get_form_submitted_message(self) -> str:
        """Get the form submission message"""
        return self.get_element_text(self.by.ID, self.message)

    def get_web_form_title(self) -> str:
        """Get web form title"""
        return self.get_page_title()

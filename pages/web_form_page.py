from bases.base_page import BasePage


class WebFormPage(BasePage):
    text_input = "my-text-id"
    submit_button = "button"
    message = "message"
    prefix_url = "/web-form.html"

    def openWebFormPage(self):
        self.open_base_url(self.prefix_url)

    def textInputField(self, input_string):
        self.write(self.by.ID, self.text_input, input_string)

    def submitButton(self):
        self.click(self.by.CSS_SELECTOR, self.submit_button)

    def getFormSubmittedMessage(self) -> str:
        return self.get_element_text(self.by.ID, self.message)

    def getWebFormTitle(self) -> str:
        return self.get_page_title()

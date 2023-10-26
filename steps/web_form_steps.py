from pages.web_form_page import WebFormPage


class WebFormSteps(WebFormPage):
    def submitTextIntoTextInputField(self, text_input: str):
        self.textInputField(text_input)
        self.submitButton()

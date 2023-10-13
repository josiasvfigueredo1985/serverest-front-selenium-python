from base.base_page import BasePage


class LoginPage(BasePage):
    url = "https://front.serverest.dev/login"

    def open(self):
        self.instance.get(self.url)

    def get_username_field(self):
        return self.instance.find_element(self.by.NAME, "username")

    def get_password_field(self):
        return self.instance.find_element(self.by.NAME, "password")

    def get_login_button(self):
        return self.instance.find_element(
            self.by.XPATH, "//button[contains(text(),'Login')]"
        )

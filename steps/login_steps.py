from pages.login_page import LoginPage


class LoginSteps(LoginPage):

    def perform_login(self, username, password):
        self.open()
        username_field = self.get_username_field()
        password_field = self.get_password_field()
        login_button = self.get_login_button()

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

import unittest
from base.base_test import TestBase
from steps.login_steps import LoginSteps


class TestLogin(TestBase):
    def test_login_success(self):
        login_steps = LoginSteps()
        login_steps.perform_login("seu_usuario", "sua_senha")


if __name__ == "__main__":
    unittest.main()

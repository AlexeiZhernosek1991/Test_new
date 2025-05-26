from pages.page_model import BasePage


class LoginPage(BasePage):
    PAGE_URL = "https://www.saucedemo.com"
    LOGIN_FILD = "Username"
    PASSWORD_FILD = 'Password'

    def enter_login(self, login):
        self.page.get_by_placeholder(self.LOGIN_FILD).fill(login)

    def enter_password(self, password):
        self.page.get_by_placeholder(self.PASSWORD_FILD).fill(password)

    def enter_button_login(self):
        self.page.get_by_role("button").click()

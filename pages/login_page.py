from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_login(self, login):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        return password_field

    def submit_click(self, flag='login'):
        if flag == 'password':
            return self.find_element(LoginPageLocators.SUBMIT_BUTTON_PASSWORD).click()
        else:
            return self.find_element(LoginPageLocators.SUBMIT_BUTTON_LOGIN).click()

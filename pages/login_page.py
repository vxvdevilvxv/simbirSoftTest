from .base_page import BasePage
from .locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    """
    Класс, описывающий страницу авторизации пользователя. Наследует класс базовой страницы.
    Реализует методы для поиска элементов на странице авторизации пользователя.
    """

    with allure.step('открытие страницы логина'):
        def enter_login(self, login):
            login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
            login_field.send_keys(login)

    with allure.step('ввод пароля'):
        def enter_password(self, password):
            password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
            password_field.send_keys(password)

    with allure.step('нажатие кнопки логин'):
        def submit_login_click(self):
            return self.find_element(LoginPageLocators.SUBMIT_BUTTON_LOGIN).click()

    with allure.step('нажатие кнопки пароль'):
        def submit_password_click(self):
            return self.find_element(LoginPageLocators.SUBMIT_BUTTON_PASSWORD).click()

from .base_page import BasePage
from .locators import MailBoxPageLocators
import allure


class MailPage(BasePage):
    """
    Класс, описывающий страницу почтового ящика. Наследует класс базовой страницы.
    Реализует методы для поиска элементов на странице почтового ящика
    """

    def __init__(self, browser):
        super().__init__(browser)
        # переопределение начальной страницы
        self.url = 'https://mail.google.com/mail/u/0/#inbox'

    with allure.step('подсчет сообщений с нужным текстом'):
        def count_of_target_massages(self, text):
            mails = self.find_elements(MailBoxPageLocators.MAIL_SUBJECT)
            return len([mail for mail in mails if text == mail.text])

    with allure.step('создание сообщения'):
        def write_mail_button_click(self):
            return self.find_element(MailBoxPageLocators.WRITE_MAIL_KEY).click()

    with allure.step('отправка сообщения'):
        def send_button_click(self):
            return self.find_element(MailBoxPageLocators.SEND_KEY).click()

    with allure.step('ввод адресата'):
        def input_destination(self, address):
            destination = self.find_element(MailBoxPageLocators.DESTINATION)
            destination.send_keys(address)

    with allure.step('ввод темы'):
        def input_topic(self, last_name):
            topic = self.find_element(MailBoxPageLocators.TOPIC)
            topic.send_keys(f'Simbirsoft Тестовое задание. {last_name}')

    with allure.step('ввод текста сообщения'):
        def input_mail_text(self, mail_text):
            mail_text_box = self.find_element(MailBoxPageLocators.MAIL_TEXT)
            mail_text_box.send_keys(mail_text)

    with allure.step('финальный тест'):
        def check_message(self, last_name):
            mails = self.find_elements(MailBoxPageLocators.MAIL_SUBJECT)
            assert f'Simbirsoft Тестовое задание. {last_name}' in mails[1].text, 'Message not found!'

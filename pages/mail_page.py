from .base_page import BasePage
from .locators import MailBoxPageLocators


class MailPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        # переопределение начальной страницы
        self.url = 'https://mail.google.com/mail/u/0/#inbox'

    def count_of_target_massages(self, text):
        mails = self.find_elements(MailBoxPageLocators.MAIL_SUBJECT)
        return len([mail for mail in mails if text == mail.text])

    def button_click(self, flag='write'):
        if flag == 'send':
            return self.find_element(MailBoxPageLocators.SEND_KEY).click()
        else:
            return self.find_element(MailBoxPageLocators.WRITE_MAIL_KEY).click()

    def input_info(self, info_text, flag):
        if flag == 'destination':
            destination = self.find_element(MailBoxPageLocators.DESTINATION)
            destination.send_keys(info_text)
            return destination
        elif flag == 'topic':
            topic = self.find_element(MailBoxPageLocators.TOPIC)
            topic.send_keys(f'Simbirsoft Тестовое задание. {info_text}')
            return topic
        elif flag == 'mail_text':
            mail_text = self.find_element(MailBoxPageLocators.MAIL_TEXT)
            mail_text.send_keys(info_text)
            return mail_text

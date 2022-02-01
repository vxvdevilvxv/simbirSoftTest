import allure
from .pages.login_page import LoginPage
from .pages.mail_page import MailPage
from .auth_data import login, password, last_name


@allure.feature('MailTest')
@allure.story('Тест входа в почтовый ящик, подсчета определенных сообщений и отправки их количества')
def test_login_and_send_message(browser):
    # открытие страницы логина
    login_page = LoginPage(browser=browser)
    login_page.open()

    # ввод логина
    login_page.enter_login(login=login)
    login_page.submit_login_click()

    # ввод пароля
    login_page.enter_password(password=password)
    login_page.submit_password_click()

    # открытие почтового ящика, т.к. идем через костыль
    mail_page = MailPage(browser)
    mail_page.open()

    # подсчет сообщений с нужным текстом'
    message_count = mail_page.count_of_target_massages(text='Simbirsoft Тестовое задание')

    # создание сообщения
    mail_page.write_mail_button_click()

    # ввод адресата
    mail_page.input_destination(address=login)

    # ввод темы
    mail_page.input_topic(last_name=last_name)

    # ввод текста сообщения
    mail_page.input_mail_text(mail_text=message_count)

    # отправка сообщения
    mail_page.send_button_click()

    # финальный тест
    mail_page.check_message(last_name=last_name)

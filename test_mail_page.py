import allure
from .pages.login_page import LoginPage
from .pages.mail_page import MailPage

login = ''
password = ''
last_name = 'Гальбинский'


@allure.feature('MailTest')
@allure.story('Тест входа в почтовый ящик, подсчета определенных сообщений и отправки их количества')
def test_login_and_send_message(browser):
    with allure.step('открытие страницы логина'):
        page = LoginPage(browser=browser)
        page.open()

    with allure.step('ввод логина'):
        page.enter_login(login=login)
        page.submit_click(flag='login')

    with allure.step('ввод пароля'):
        browser.implicitly_wait(2)
        page.enter_password(password=password)
        page.submit_click(flag='password')

    with allure.step('открытие почтового ящика, т.к. идем через костыль'):
        page = MailPage(browser)
        page.open()

    with allure.step('подсчет сообщений с нужным текстом'):
        message_count = page.count_of_target_massages(text='Simbirsoft Тестовое задание')

    with allure.step('создание сообщения'):
        page.button_click(flag='write')

    with allure.step('ввод адресата'):
        page.input_info(info_text=login, flag='destination')

    with allure.step('ввод темы'):
        page.input_info(info_text=last_name, flag='topic')

    with allure.step('ввод текста сообщения'):
        page.input_info(info_text=message_count, flag='mail_text')

    with allure.step('отправка сообщения'):
        page.button_click(flag='send')

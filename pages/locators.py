from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, '#identifierId')
    PASSWORD_FIELD = (By.NAME, 'password')
    SUBMIT_BUTTON_LOGIN = (By.CSS_SELECTOR, '#identifierNext')
    SUBMIT_BUTTON_PASSWORD = (By.CSS_SELECTOR, '#passwordNext')


class MailBoxPageLocators:
    MAIL_SUBJECT = (By.CSS_SELECTOR, 'span.bqe')
    WRITE_MAIL_KEY = (By.CSS_SELECTOR, 'div[role=button][jslog~="20510;"]')
    DESTINATION = (By.CSS_SELECTOR, "div[role=presentation] input")
    TOPIC = (By.NAME, 'subjectbox')
    MAIL_TEXT = (By.CSS_SELECTOR, 'div[role=textbox]')
    SEND_KEY = (By.CSS_SELECTOR, 'div[role=button][aria-label~="Отправить"]')

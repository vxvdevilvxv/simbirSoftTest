from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, '#identifierId')
    PASSWORD_FIELD = (By.NAME, 'password')
    SUBMIT_BUTTON_LOGIN = (By.CSS_SELECTOR, '#identifierNext')
    SUBMIT_BUTTON_PASSWORD = (By.CSS_SELECTOR, '#passwordNext')

class MailBoxPageLocators:
    MAIL_SUBJECT = (By.CSS_SELECTOR, 'span.bqe')
    WRITE_MAIL_KEY = (By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
    DESTINATION = (By.CSS_SELECTOR, "div[role=presentation] input")
    TOPIC = (By.NAME, 'subjectbox')
    MAIL_TEXT = (By.CSS_SELECTOR, 'div[role=textbox]')
    SEND_KEY = (By.XPATH, '/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]')

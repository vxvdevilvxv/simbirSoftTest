from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        # костыль для обхода защиты гугла
        self.url = 'https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A609%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A44d40d09a5dfe6b1%2C10%3A1643560439%2C16%3Ab2baa76bbb30987d%2Cfcf694d5925dc7267b4dc46d26697f0a852c5f9a5e144e9d0c3f56ab2fe0ccec%22%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%226b7736cc7452437a87f0ca803ebed279%22%7D&response_type=code&flowName=GeneralOAuthFlow'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def open(self):
        self.browser.get(self.url)

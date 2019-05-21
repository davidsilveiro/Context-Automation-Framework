from selenium.webdriver.common.by import By
from base_page_object import BasePage


class AutomationLoginPage(BasePage):
    locator_dictionary = {
        "email": (By.ID, 'id_username'),
        "password": (By.ID, 'id_password'),
        "signin_button": (By.NAME, 'login'),
        "welcome": (By.CLASS_NAME, 'container'),
        "uploadPage": (By.XPATH, "/html/body/nav/div/ul[1]/li/a")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="127.0.0.1:8000")

    def login(self,username,passwd):
        self.find_element(*self.locator_dictionary['email']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['signin_button']).click()
        

    def get_text(self):
        self.find_element(*self.locator_dictionary['welcome']).text

    def nav_upload(self):
        self.find_element(*self.locator_dictionary['uploadPage']).click()
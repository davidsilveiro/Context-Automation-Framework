from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
from time import sleep

class BasePage(object):

    def __init__(self, browser, base_url='127.0.0.1:8000'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 10

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self,url):
        self.browser.get(url) 

    def hover(self,element):
            ActionChains(self.browser).move_to_element(element).perform()
            # I don't like this but hover is sensitive and needs some sleep time
            time.sleep(5)

    def __getattr__(self, item):
        try:
            if item in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser,self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser,self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()

                return self.find_element(*self.locator_dictionary[item])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(item)

    def method_missing(self, item):
        print("No %s here!"%item)
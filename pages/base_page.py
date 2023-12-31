from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import BasePageLocator

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
#
    def open(self):
        self.browser.get(self.url)
#
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocator.BASKET_LINK)
        basket_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return

        # Другие методы и элементы

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocator.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

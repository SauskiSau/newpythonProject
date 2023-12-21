
from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()



    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def check_current_url_for_login_substring(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"URL {current_url} does not contain the substring 'login'"


from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert LoginPageLocators.LOGIN_URL_SUBSTRING in current_url, f"URL {current_url} не содержит подстроку 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена на странице"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
#dxghsdfghfghdfj

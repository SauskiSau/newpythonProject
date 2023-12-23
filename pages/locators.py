from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "i.icon-signin")
#
# class LoginPageLocators:
#     LOGIN_FORM = (By.CLASS_NAME, "login_form")
#     REGISTER_FORM = (By.CLASS_NAME, "register_form")
#     LOGIN_URL_SUBSTRING = "login"

class BasketPageLocator():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "availability")

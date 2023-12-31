from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "i.icon-signin")

class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
    LOGIN_URL_SUBSTRING = "login"

    EMAIL_INPUT = (By.ID, "id_login-username")
    PASSWORD_INPUT = (By.ID, "id_login-password")
    REGISTER_BUTTON = (By.NAME, "login_submit")

class BasketPageLocator():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")  #availability     #alertinner
    BASKET_LINK = (By.CLASS_NAME, "btn btn-default")  # кнопка карзины
class BasePageLocator():
    BASKET_ITEMS = (By.CLASS_NAME, "instock") #Корзина не пуста, а должна быть
    BASKET_EMPTY_MESSAGE = (By.CLASS_NAME, "btn btn-defaultee") #Нет сообщения о том, что корзина пуста
    BASKET_LINK = (By.CLASS_NAME, "btn btn-default")  # кнопка карзины
    USER_ICON = (By.CSS_SELECTOR, "wicon") #user loged in
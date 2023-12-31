from .pages.product_page import ProductPage
from .pages.locators import BasketPageLocator
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocator
from .pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

import time
import math
import pytest

# @pytest.mark.parametrize('link',
link_values = [ "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"]
# #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Bug in offer1")),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"]
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
@pytest.mark.parametrize('link', link_values)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.solve_quiz_and_get_code()      #page.should_be_login_link()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_basket_is_empty()

#     # Пример использования WebDriverWait
@pytest.mark.parametrize('link', link_values)
class TestThreetest():
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.is_not_element_present(
            *BasketPageLocator.SUCCESS_MESSAGE), "Success message is present, but should not be"
    def test_guest_cant_see_success_message(browser, link):
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(
            *BasketPageLocator.SUCCESS_MESSAGE), "Success message is present, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.is_disappeared(
            *BasketPageLocator.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
@pytest.mark.parametrize('link', link_values)
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "somepassword"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    def test_user_cant_see_success_message(browser, link):
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(
            *BasketPageLocator.SUCCESS_MESSAGE), "Success message is present, but should not be"
    def test_user_can_add_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()

    def test_guest_can_go_to_login_page_from_product_page(self):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
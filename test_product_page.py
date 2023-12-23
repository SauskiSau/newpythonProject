from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    # Пример использования WebDriverWait

        # Ожидание, пока элемент не станет кликабельным

    # 2. Создаем объект ProductPage для работы с этой страницей.

    # 3. Используем метод add_to_basket для добавления товара в корзину.
    page.add_to_basket()

    time.sleep(3)
    #
    # # 4. Используем метод should_be_success_message для проверки сообщения о добавлении.
    # page.should_be_success_message()
    #
    # # 5. Используем метод solve_quiz_and_get_code для получения проверочного кода и ввода его в ответ на задание.
    #
    # # 6. Добавляем проверку на ожидаемый результат, например, сравнение стоимости корзины с ценой товара.
    # page.should_be_basket_price_equal_to_product_price()

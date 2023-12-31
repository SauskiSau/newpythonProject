from .base_page import BasePage
from .locators import BasketPageLocator

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_ITEMS), \
            "Basket is not empty, but should be"  #Корзина не пуста, а должна быть

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_EMPTY_MESSAGE), \
            "No message that basket is empty" #Нет сообщения о том, что корзина пуста

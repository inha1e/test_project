from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is not empty!"

    def basket_is_empty_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty Basket Message was not found!"
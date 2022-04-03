from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def product_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
    
    def is_correct_product_in_basket(self):
        assert self.product_name() == self.product_in_basket(), "Product in basket isn't equal product on page!!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message wasn't disappeared"
       

    
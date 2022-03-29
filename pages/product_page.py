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
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT).text
        return product_name

    def product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return product_price

    def product_in_basket(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        return product_in_basket
    
    def is_correct_product_in_basket(self):
        assert self.product_name() == self.product_in_basket(), "Product in basket isn't equal product on page!!"

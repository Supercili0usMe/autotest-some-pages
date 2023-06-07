from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
    
    def should_be_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert product_name == added_name, "Product name doesn't match the added product"

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert product_price == added_price, "Product price doesn't equals the added product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but shouldn't be"
    
    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message isn't disappear, but should be"
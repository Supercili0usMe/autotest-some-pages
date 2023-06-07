from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_any_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
        "Found some products in basket, but shouldn't be"
    
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
        "Didn't found empty bucket text"